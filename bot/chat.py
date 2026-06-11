from openai import RateLimitError
from google.genai import types
from google.genai.errors import ClientError
from database import connection
from functions import summary, PConnections
from functions.emotions import emotions 
from bot import client
from bot import modes
from bot.Image import Image
from google.api_core.exceptions import ServerError
from Exceptions import exceptions
from functions import jokes
from groq import Groq
import json

cache = []
minimo = 0
resposta_final = ""
connection.cursor.execute('select mode from settings where id = 1')
result = connection.cursor.fetchone()
connection.cursor.fetchall()

with open(r"functions\tools.json", "r", encoding="utf-8") as f:
    groq_tools = json.load(f)

if result:
    current_mode = result[0]
else:
    current_mode = 'modo_normal'

def enviar_menssagem(question):
    global current_mode
    resposta_final = ""

    memoria_resumida = summary.resumir()
    cache.append(summary.cache_localU(question))

    emotions.losing_emotions()
    emotions.verify(question)
    r = emotions.emotion_level()

    contexto_emocional = f"""

        Current emotional state:
        {r}

        Behavior:
        - emotions affect tone naturally
        - never mention emotions explicitly
        - strongest emotions dominate behavior
    """

    contexto_local = f"""
        memory:
        {memoria_resumida}

        last 5 mg of yours and the user's:
        {cache}
        
        current question:
        {question}
    """
    
    if "/modo normal" in question:
        current_mode = "modo_normal"
        connection.cursor.execute('update settings set mode = "modo_normal" where id = 1')
        connection.meudb.commit()
    elif "/modo tecnico" in question:
        current_mode = "modo_tecnico"
        instruction = modes.modo_tecnico
        connection.cursor.execute('update settings set mode = "modo_tecnico" where id = 1')   
        connection.meudb.commit()
    elif "/emotions" in question:
        print(r)    

    if current_mode == "modo_normal":
        instruction = modes.modo_normal
    elif current_mode == "modo_tecnico":
        instruction = modes.modo_tecnico     

    final_instruction = instruction + contexto_emocional
    try:
        try:
            enviar = client.groq.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": final_instruction},
                    {"role": "user", "content": contexto_local}
                ],
                tools=groq_tools,
                stream=True,                
            )
        except ServerError:
            raise exceptions.altaDemanda()

    except RateLimitError as e:
        print(f"detalhes do erro: {e}")
        print("Mya: Mya is so tired.... (API limit hit, try again after 60 seconds)")
        return
    
    except exceptions.altaDemanda as e:
        print(e)
    
    try:
        print("Mya: ", end='', flush=True)
        tool_calls = []

        for chunk in enviar:
            if chunk.choices and chunk.choices[0].delta.content:
                texto = chunk.choices[0].delta.content
                print(texto, end="", flush=True)
                resposta_final += texto

            if chunk.choices and chunk.choices[0].delta.tool_calls:
                delta_tools = chunk.choices[0].delta.tool_calls
                for tool_call in delta_tools:
                    if len(tool_calls) <= tool_call.index:
                        tool_calls.append(tool_call)
                    else:
                        if tool_call.function.arguments:
                            tool_calls[tool_call.index].function.arguments += tool_call.function.arguments

        print() 
        
        if tool_calls:
            import json
            for chamada in tool_calls:
                func_obj = getattr(chamada, 'function', None)
                nome_funcao = getattr(func_obj, 'name', None) if func_obj else None
                
                if not nome_funcao:
                    continue

                args_str = getattr(func_obj, 'arguments', '{}')
                argumentos = json.loads(args_str) if args_str else {}

                match nome_funcao:
                    case "abrirPrograma":
                        PConnections.abrirPrograma(argumentos.get("programa"))
                    case "Pesquisar":
                        PConnections.Pesquisar(argumentos.get("termo"))
                    case "fechar":
                        PConnections.fechar(argumentos.get("programa"))
                    case "comandos":
                        PConnections.comandos(argumentos.get("comando"))
                    case "repouso":
                        PConnections.repouso()
                    case "tocarMusica":
                        PConnections.tocarMusica(argumentos.get("musica"))
                    case "piada":
                        jokes.piada()
                        return
                    case "gerarImagem":
                        Image.gerarImagem(argumentos.get("descricao"))

        resposta_final = resposta_final.replace('"', '')
        cache.append(summary.cache_localI(resposta_final))
        return resposta_final
    
    except Exception as e:
        print(f"\nErro ao processar stream da Groq: {e}")