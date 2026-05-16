from openai import RateLimitError
from google.genai import types
from google.genai.errors import ClientError
from database import connection
from functions.emotions import emotions 
from ia import client
from ia import modes


resposta_final = ""
connection.cursor.execute('select mode from settings where id = 1')
current_mode = connection.cursor.fetchone()[0]
connection.cursor.fetchall()

def enviar_menssagem(question):
    global current_mode
    resposta_final = ""

    connection.cursor.execute('select role,message from memory order by id desc limit 50')
    memoria_bruta = connection.cursor.fetchall()
  
    memoria = []

    emocao = str(emotions.verify(question))

    contexto_emocional = (
        f"\n\n[CONTEXTO EMOCIONAL ATUAL DA MYA]\n"
        f"Estes são os seus níveis atuais de sentimento em resposta à última mensagem do usuário: {emocao}.\n"
        f"Instrução: Adapte o tom da sua resposta de forma natural a esses sentimentos. "
        f"Se 'sadness' estiver alto, seja empática e acolhedora. Se 'angry' estiver alto, responda de forma mais fria ou ríspida. "
        f"Não cite os números da sua emoção explicitamente na resposta, apenas sinta e expresse no seu tom de fala."
    )

    for a, b in reversed(memoria_bruta):

        papel = 'user' if a.lower() == 'user' else 'model'
        memoria.append(
            types.Content(
                role=papel,
                parts=[types.Part(text=b)]
            )
    )
    
    if "/modo normal" in question:
        current_mode = "modo_normal"
        connection.cursor.execute('update settings set mode = "modo_normal" where id = 1')
        connection.meudb.commit()
    elif "/modo tecnico" in question:
        current_mode = "modo_tecnico    "
        instruction = modes.modo_tecnico
        connection.cursor.execute('update settings set mode = "modo_tecnico" where id = 1')   
        connection.meudb.commit()
    elif "/emotions" in question:
        print(emocao)    

    if current_mode == "modo_normal":
        instruction = modes.modo_normal
    elif current_mode == "modo_tecnico":
        instruction = modes.modo_tecnico     

    final_instruction = instruction + contexto_emocional
    try:
        enviar = client.gemini.models.generate_content_stream(
            model="gemini-2.5-flash-lite",
            contents=memoria,
            config={
                "system_instruction": final_instruction
            }
        )

    except RateLimitError:
        print("Mya sleeping.... (rate limit hit, try again later)")
        return
    
    try:
        print("Mya: ", end='', flush=True)
        for chunk in enviar:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                resposta_final += chunk.text
        print()    
        resposta_final = resposta_final.replace('"', '')

        return resposta_final
    
    except ClientError:
        print("Mya is so tired.... (API limit hit, try again after 60 seconds)")