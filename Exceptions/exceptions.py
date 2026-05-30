class ProgramaNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("Programa nao encontrado")
        