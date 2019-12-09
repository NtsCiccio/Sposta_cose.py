from os import system, name

def clean_tha_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')