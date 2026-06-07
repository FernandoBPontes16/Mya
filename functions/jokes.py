import requests

def piada():
    """
    Use this function when the user asks for a joke or something funny;
    and don't say anything, this function will say a joke.
    """
    response = requests.get("https://v2.jokeapi.dev/joke/Any?lang=pt")
    msg = response.json()
    piada = msg['setup']
    resposta = msg['delivery']
    piadaCompleta = piada + " resposta: " + resposta
    print(f'{piadaCompleta}')