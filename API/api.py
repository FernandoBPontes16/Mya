from fastapi import FastAPI
from functions import memory
from bot import chat
from bot.Image import Image

app = FastAPI()

@app.get("/")
def home():
    return {'status': 'online'}

@app.get("/q={question}/Image={imageCondition}")
def EnviarPergunta(question: str, imageCondition: bool):
    if imageCondition == True:
        memory.salvarDB('user', question)
        q = question + " Create a description for a Image generate with this(You weren't going to generate an image; just create the decision/prompt for an image.Don't say what you think about it; return to the image description without emotion or anything like that.)."
        r = chat.enviar_menssagem(question)
        d = chat.enviar_menssagem(q)
        i = Image.gerarImagem(d)
        memory.salvarDB('Mya', r)
        return {'Mya': r, 'Image': i}
    else:    
        memory.salvarDB('user', question)
        r = chat.enviar_menssagem(question)
        memory.salvarDB('Mya', r)
        return {'Mya': r}