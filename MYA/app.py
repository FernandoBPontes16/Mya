from functions import memory
from ia import chat

while True:
    question = input("User: ")
    
    if question == "/exit":
        break

    memory.salvarDB('user', question)
    resposta = chat.enviar_menssagem(question)
    memory.salvarDB('Mya', resposta)