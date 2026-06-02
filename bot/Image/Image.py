import requests
from Exceptions import exceptions

valor1 = "https://image.pollinations.ai/prompt/"
valor2 = "model=flux-2&key=sk_Ud5qObsCefTtDl468apY24YTzC435JT7"
#cat?

def gerarImagem(parametros: str):
    """
    Triggers the generation of an image based on the user's request.
    Use this function IMMEDIATELY whenever the user explicitly asks to create, 
    generate, or draw an image, photo, or visual illustration.
    Args:
        parametros (str): A space-separated list of visual elements, keywords, 
                          and descriptions requested by the user for the image.
                          Do not include conversational words like "please" or "generate".
                          Example: "dog cute farm sunset"
    """
    global valor1,valor2
    try:
        parametrosList = parametros.split()
        for i in range(len(parametrosList)):
            if i == len(parametrosList)-1:
                valor1 = valor1 + parametrosList[i]
            else:    
                valor1 = valor1 + parametrosList[i] + "%20"
        valor1 = valor1 + valor2
        try:
            r = requests.get(valor1)
            with open(r'C:\Users\User\Documents\MyaV2\bot\Image\Image.png', 'wb') as f:
                f.write(r.content)
        except requests.exceptions.RequestException or Exception:
            raise exceptions.ImagemNaoGerada()        
    except exceptions.ImagemNaoGerada as e:
        print(e)     