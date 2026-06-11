import subprocess
import os
import pyautogui
import time
from Exceptions import exceptions
import ctypes

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
    try:
        try:
            subprocess.Popen(nome)

        except FileNotFoundError:
            raise exceptions.ProgramaNaoEncontrado()     
        
    except exceptions.ProgramaNaoEncontrado as e:
        print(e)
        a = buscarLocal(nome)
        subprocess.Popen(a, shell=True)

def Pesquisar(pesquisa: str,navegador: str):
    """
    The Search(search, browser) function opens the specified browser and types the search term into the internet.
    Strictly generate the function call with the arguments identified in the user's text:
    Search(search="term_here", browser="browser_here")
    If the browser is not mentioned, fill in the browser argument with "chrome". Return only the line of code, without markdown or explanations.
    When asked to open a website or go to a website, put the website's URL instead of the search bar.
    """
    if navegador.lower() == "chrome" or navegador.lower() == "google":
        subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    else:    
        pyautogui.press('win')
        pyautogui.write(navegador)
        pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('crtl', 'l')
    pyautogui.write(pesquisa, interval=0.1)
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

def comandos(comando: str):
    """
    This function is used to run data in the command prompt (cmd). 
    If the user asks to create a file, folder, etc.
    use the command in cmd correctly and create it with the name they request or the context of what they want the file or folder for. 
    This can also be used to rename files or folders. 
    Think of this function as allowing you to execute functions within the command prompt; 
    it won't specify what they are, you'll have to know. It can be anything that can be done in cmd.
    return only the command that will be executed in cmd.
    """
    subprocess.run(comando,shell=True)

def repouso():
    """
    This function is only used to put the user's PC into sleep mode indefinitely until the user presses a key.
    """
    ctypes.windll.powrprof.SetSuspendState(0, 0, 0)

def tocarMusica(pesquisa: str):
    """
    This function is used to play music; 
    retrieve only the song title requested by the user, 
    and if necessary, the artist/band as well. 
    Do not remove any part of the song title.
    ex:
        -user: play usseewa
        -mya: ok!
    you will return: usseewa
    """
    subprocess.Popen(r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe")
    time.sleep(6)
    pyautogui.hotkey('ctrl','l')
    pyautogui.write(pesquisa, interval=0.2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('tab')
    for i in range(4):
        pyautogui.press('right')
        time.sleep(0.2)
    pyautogui.press('enter')    