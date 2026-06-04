from openai import RateLimitError
from google.genai import types
from google.genai.errors import ClientError
from database import connection
from functions import summary, PConnections
from functions.emotions import emotions 
from bot import client
from bot import modes
from bot.Image import Image

cache = []
minimo = 0
resposta_final = ""
connection.cursor.execute('select mode from settings where id = 1')
result = connection.cursor.fetchone()
connection.cursor.fetchall()


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
        enviar = client.gemini.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=contexto_local,
            config={
                "system_instruction": final_instruction,
                "tools": [PConnections.abrirPrograma,
                          PConnections.Pesquisar,
                          PConnections.fechar,
                          PConnections.comandos,
                          PConnections.repouso,
                          PConnections.tocarMusica
                          #Image.gerarImagem
                          ]            
            },                
        )

    except RateLimitError as e:
        print(f"detalhes do erro: {e}")
        print("Mya: Mya is so tired.... (API limit hit, try again after 60 seconds)")
        return
    
    try:
        print("Mya: ", end='', flush=True)
        for chunk in enviar:
            if chunk.function_calls:
                for call in chunk.function_calls:
                    match call.name:
                        case "abrirPrograma":
                            argumentos = call.args
                            PConnections.abrirPrograma(argumentos)
                        case "Pesquisar":
                            argumentos = call.args
                            PConnections.Pesquisar(argumentos)
                        case "fechar":
                            argumentos = call.args
                            PConnections.fechar(argumentos)
                        case "comandos":
                            argumentos = call.args
                            PConnections.comandos(argumentos)
                        case "repouso":
                            PConnections.repouso()
                        case "tocarMusica":
                            argumentos = call.args
                            PConnections.tocarMusica(argumentos)
                        case "gerarImagem":
                            argumentos = call.args
                            Image.gerarImagem(argumentos)    
            elif chunk.text:
                print(chunk.text, end="", flush=True)
                resposta_final += chunk.text
        print()    
        resposta_final = resposta_final.replace('"', '')
        cache.append(summary.cache_localI(resposta_final))
        return resposta_final
    
    except ClientError as e:
        print(f"detalhes do erro: {e}")
        print("Mya is so tired.... (API limit hit, try again after 60 seconds)")