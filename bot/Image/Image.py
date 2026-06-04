from bot import client

def gerarImagem(prompt: str):
    response = client.gemini.models.generate_content(
        model="gemini-3.1-flash-image",
        contents=prompt
    )

    for part in response.parts:
        image = part.as_image()
        image.save(r'bot\Image\Gen.png')
