import subprocess
import os
import pyautogui
import time

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

def Pesquisar(pesquisa: str,navegador: str):
    """
    The Search(search, browser) function opens the specified browser and types the search term into the internet.
    Strictly generate the function call with the arguments identified in the user's text:
    Search(search="term_here", browser="browser_here")
    If the browser is not mentioned, fill in the browser argument with "chrome". Return only the line of code, without markdown or explanations.
    When asked to open a website or go to a website, put the website's URL instead of the search bar.
    """
    if navegador.lower() == "chrome":
        subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    else:    
        pyautogui.press('win')
        pyautogui.write(navegador)
        pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.click(691, 582)
    pyautogui.write(pesquisa)
    pyautogui.press('enter')

def fechar(app: str):
    """
    This function is used to close a specific application. 
    The user will request to close an app, and you will return only the app's name without spaces, 
    but with the correct spelling as the .exe file is saved.
    If it's a system app that might cause damage or harm, prevent it from running and explain the problem. 
    If it's an application that doesn't use .exe, use its method.
    If the application closes successfully, simply return the message: Application closed successfully.
    """
    subprocess.Popen(f'taskkill /f /im {app} >nul 2>&1')

#Nao funcionando 
def tocarMusica(pesquisa: str):
    """
    This function opens Spotify and plays the song requested by the user.
    CRITICAL RULE FOR THE ARGUMENT:
    - The 'pesquisa' argument must contain ONLY the clean name of the song and artist.
    - STRICTLY REMOVE all conversational text, commands, and trigger words like 'toca', 'tocar', 'a musica', 'play', 'mya', 'de', 'por favor'.
    Example: If the user says "mya toca a musica what is love de twice pode ser?", 
    the 'pesquisa' argument value MUST BE EXACTLY: "what is love twice"
    """
    subprocess.Popen(r'cd "AppData\Roaming\Microsoft\Windows\Start Menu\Programs" && start Spotify')
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(pesquisa)
    pyautogui.press('tab')
    for i in range(4):
        pyautogui.press('right')
    pyautogui.press('enter')    
