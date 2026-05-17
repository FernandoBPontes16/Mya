from database import connection
from ia import client

connection.cursor.execute('select role,message from memory order by id desc limit 20')
memoria = connection.cursor.fetchall()

def resumir():
        contexto = f"""
        Voce deve resumir tudo que contem nessa menssagem e so mander conteudos importantes
        {memoria}
        """
        response = client.gemini.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=contexto
        )
        return response.text
    