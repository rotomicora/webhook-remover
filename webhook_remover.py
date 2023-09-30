import os, requests, fade ;from colorama import Fore;from pystyle import * # Importamos las librerias que utilizaremos
w = Fore.LIGHTWHITE_EX;r = Fore.LIGHTRED_EX;g = Fore.LIGHTGREEN_EX;y = Fore.LIGHTYELLOW_EX;b = Fore.LIGHTBLUE_EX;m = Fore.LIGHTMAGENTA_EX;c = Fore.LIGHTCYAN_EX;black = Fore.LIGHTBLACK_EX # Definimos unas variables para los colores de la libreria Fore

# Las dos "GUI" que utilizaremos para estilizar el programa un poco
gui = """
    
            ╔═══════════════════════════════════════════════╗
            ║                                          . ╔══╣
            ║   ╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═                  ╚═╝  ║
            ║   ║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗                       ║
            ║   ╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩     ╦  ╦  ╗           ║
            ║  ╦═╗╔═╗╔╦╗╔═╗╦  ╦╔═╗╦═╗     ╚╗╔╝  ║           ║
            ║  ╠╦╝║╣ ║║║║ ║╚╗╔╝║╣ ╠╦╝      ╚╝   ╩           ║
            ║  ╩╚═╚═╝╩ ╩╚═╝ ╚╝ ╚═╝╩╚═                       ║
            ╠══╗  .                .                  .     ║
            ╠╗   ╔╩═╗         ╔╩═╦═╩ ·               ╔╩═╗   ║
            ╚╩═══╩═══════════════╩══════════════════════╩═══╝
"""
gui_animated = """
╔═══════════════════════════════════════════════╗
║                                          . ╔══╣
║   ╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═                  ╚═╝  ║
║   ║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗                       ║
║   ╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩     ╦  ╦  ╗           ║
║  ╦═╗╔═╗╔╦╗╔═╗╦  ╦╔═╗╦═╗     ╚╗╔╝  ║           ║
║  ╠╦╝║╣ ║║║║ ║╚╗╔╝║╣ ╠╦╝      ╚╝   ╩           ║
║  ╩╚═╚═╝╩ ╩╚═╝ ╚╝ ╚═╝╩╚═                       ║
╠══╗  .                .                  .     ║
╠╗   ╔╩═╗         ╔╩═╦═╩ ·               ╔╩═╗   ║
╚╩═══╩═══════════════╩══════════════════════╩═══╝
           Press enter for continue
"""
os.system("@mode con cols=150, lines=45 & cls & title Webhook Delenter v1.0 ") # Definimos el tamaño de la terminal, limpiamos la terminal y asignamos un titulo a la terminal
Anime.Fade(Center.Center(gui_animated), Colors.rainbow, Colorate.Vertical, interval=0.1, enter=True) # Hacemos una animacion de la "GUI" que definimos anteriormente
faded_gui = fade.pinkred(gui) # Hacemos un fade a la "GUI" que definimos anteriormente

os.system("cls")
print(faded_gui) # Imprimimos la "GUI" que definimos anteriormente

def webhook_remover(): # Definimos la funcion webhook_remover
    webhook = input(f"{m}[{w}>{m}] {black}Webhook: {w}") # Pedimos el webhook
    try: # Intentamos hacer lo siguiente
        requests.delete(webhook) # Eliminamos el webhook
        print(f"{w}[{w}OK{w}] {black}Webhook eliminada correctamente") # Imprimimos un mensaje de que se ha eliminado correctamente
    except: # Si no se ha podido hacer lo anterior, se ejecutara lo siguiente
        print(f"{m}[{w}ERROR{m}] {black}Ha ocurrido un error") # Imprimimos un mensaje de error

webhook_remover() # Llamamos a la funcion webhook_remover
