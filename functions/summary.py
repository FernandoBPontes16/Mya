#from database import connection
#from ia import client
import google.genai.errors

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

minimo = 0
response_local = None
cache = []

#teste
gemini = genai.Client(api_key="AIzaSyCUmvBMeZP-ljDD8dOzyFr59pVUhciU1VM")
text = """Lucas: Fala irmão! Tudo certo? Vamos fechar aquele churrasco no próximo sábado?Mateus: Fala cara! Beleza pura. Vamos fechar sim, já passou da hora! Vai ser na sua casa?Lucas: Vai ser aqui sim, a partir das 13h. O que você acha de a gente rachar a carne e cada um leva o que for beber?Mateus: Fechado, esquema perfeito. O que eu levo de carne? Posso comprar uma picanha ou uma fraldinha, você escolhe.Lucas: Pô, se achar uma picanha bonita no preço, manda bala! Eu cuido do carvão, do acompanhamento (pão de alho e vinagrete) e pego uma maminha também.Mateus: Demorou! Fechadíssimo. Mais alguém vai colar com a gente?Lucas: Chamei o Thiago e a Marina também, eles confirmaram. Vai dar um grupo bom!Mateus: Show de bola! Sábado 13h estou aí sem falta. Valeu pelo convite!Lucas: Tamo junto, mano! Até sábado! 👊"""

def cache_local(question):
        global cache
        if len(cache) > 5:
                del cache[0]        
        cache.append(f'user: {question}')
        return cache


def resumir():
        global minimo, response, response_local
        minimo += 1
        try:
                if minimo >= 5 or response_local == None:
                        #connection.cursor.execute('select role,message from memory order by id desc limit 20')
                        #memoria = connection.cursor.fetchall()


                        contexto = f"""
                        You must summarize everything contained in this message and only send important content.
                        CRITICAL RULE: NEVER delete or ignore name changes, nicknames, or personal information that the user has revealed about themselves (e.g., if they asked to be called by another name, this MUST be explicitly stated in the summary).
                        {text}
                        """
                        response = gemini.models.generate_content(
                                model="gemini-2.5-flash-lite",
                                contents=contexto
                        )
                        minimo = 1
                        response_local = response.text
                        resumo = f"""
                        summary conversations:
                        {response_local}
                        """
                        return resumo

        except google.genai.errors.ServerError:
                minimo -= 1
                print('Mente da Mya ficou sobrecarregada... Pegando uma save de memoria')
                response_local = response.text
                return response_local
for i in range(3):
        print(minimo)
        a = resumir()
        print(a)