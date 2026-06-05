VERMELHO_NEGRITO = "\033[1;31m"
AMARELO_NEGRITO = "\033[1;33m"
CIANO_NEGRITO = "\033[1;36m"
RESET = "\033[0m"

class ProgramaNaoEncontrado(Exception):
    def __init__(self):
        mensagem = f"{AMARELO_NEGRITO}Programa não encontrado, irei procurar em outro local, aguarde um minuto{RESET}"

        super().__init__(mensagem)

class ImagemNaoGerada(Exception):
    def __init__(self):
        mensagem = f"{CIANO_NEGRITO}Imagem não gerada por algum motivo tente novamente daqui alguns minutos{RESET}"

        super().__init__(mensagem)        

class altaDemanda(Exception):
    def __init__(self):
        mensagem = f"{VERMELHO_NEGRITO} [MYA ERRO]: Mya esta com alta demanda de mensagens... Tente novamente mais tarde {RESET}"

        super().__init__(mensagem)        