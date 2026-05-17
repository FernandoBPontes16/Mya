from database import connection
from ia import client
import google.genai.errors

minimo = 0
response_local = None
cache = []

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
                        connection.cursor.execute('select role,message from memory order by id desc limit 20')
                        memoria = connection.cursor.fetchall()


                        contexto = f"""
                        You must summarize everything contained in this message and only send important content.
                        CRITICAL RULE: NEVER delete or ignore name changes, nicknames, or personal information that the user has revealed about themselves (e.g., if they asked to be called by another name, this MUST be explicitly stated in the summary).
                        {memoria}
                        """
                        response = client.gemini.models.generate_content(
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
        return response_local