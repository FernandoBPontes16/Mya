from openai import RateLimitError
from google.genai import types
from google.genai.errors import ClientError
from database import connection
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

    if current_mode == "modo_normal":
        instruction = modes.modo_normal
    elif current_mode == "modo_tecnico":
        instruction = modes.modo_tecnico     

    try:
        enviar = client.gemini.models.generate_content_stream(
            model="gemini-2.5-flash-lite",
            contents=memoria,
            config={
                "system_instruction": instruction
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