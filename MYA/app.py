from ollama import chat
import mysql.connector
import time
from openai import RateLimitError
from google import genai
from google.genai import types
from google.genai.errors import ClientError

memory = ""


client = genai.Client(api_key="API_KEY")

meudb = mysql.connector.connect(    
    user='YOUR_USER',
    password='YOUR_PASSWORD',
    host='YOUR_HOST',
    database='YOUR_DATABASE'
)
cursor = meudb.cursor()

def falar():

    print

def enviar_menssagem():
    global memory, p
    memory = ""

    cursor.execute('select role,message from memory order by id desc limit 10')
    memoria_bruta = cursor.fetchall()
  
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
        enviar = client.models.generate_content_stream(
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
                memory += chunk.text
                time.sleep(0.05)   
        print()    
        memory = memory.replace('"', '')    
        salvarDB(memory)
    except ClientError:
        print("Mya is so tired.... (API limit hit, try again after 60 seconds)")

def salvarDB(a):
    if a == None:
        cursor.execute(f'insert into memory (role, message) value ("user", "{question}") ')
        meudb.commit()

    else:    
        cursor.execute(f'insert into memory (role, message) value ("Mya", "{a}") ')
        meudb.commit()

while True:
    question = input("User: ")
    salvarDB(None)

    if question == "/exit":
        break

    else:
        enviar_menssagem()
    