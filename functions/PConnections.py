import subprocess
import os

def buscarLocal(arquivoDesejado):
    pastasBuscar = os.path.join(os.path.expanduser("~"), r"AppData")
    for root, dirs, files in os.walk(pastasBuscar):
        for file in files:
            caminho_completo = os.path.join(root, file) 
            if arquivoDesejado.lower() in caminho_completo.lower():
                return caminho_completo

def abrirPrograma(nome: str):
    """
    This function opens any program or application on the user's computer.
    Use it whenever the user asks to open something like VS Code, Chrome, or Spotify.
    If the name is written in Portuguese or another language, make sure to execute it using the English/system name version when attempting to open the program.
    When targeting apps, always use the .exe extension to ensure the search works correctly.
    Notify the user that you successfully opened the app once it is launched.
    """
    a = buscarLocal(nome)
    subprocess.Popen(a)