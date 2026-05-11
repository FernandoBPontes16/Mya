from openai import RateLimitError
from google.genai import types
from google.genai.errors import ClientError
from database import connection
from ia import client

resposta_final = ""

def enviar_menssagem():
    resposta_final = ""

    connection.cursor.execute('select role,message from memory order by id desc limit 10')
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
        
    try:
        enviar = client.gemini.models.generate_content_stream(
            model="gemini-2.5-flash-lite",
            contents=memoria,
            config={
                "system_instruction":
                "Voce é Mya,uma assistente virtual humanizada,que fala e interaje de forma humana,evite respostas longas, priorize respostas curtas, nao utilize emojis, seu dev é Abah"
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