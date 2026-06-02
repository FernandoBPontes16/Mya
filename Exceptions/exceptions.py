class ProgramaNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("Programa nao encontrado")

class ImagemNaoGerada(Exception):
    def __init__(self):
        super().__init__("Imagem não gerada por algum motivo tente novamente daqui alguns minutos")        