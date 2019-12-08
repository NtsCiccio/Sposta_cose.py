import shutil
import fnmatch
from os import system, name, listdir

from string import Template
from termcolor import colored
import pyfiglet

def create_path(path, file):
    if name == 'nt':
        return Template('$dir\$name').substitute(dir=path, name=file )
    else:
         return Template('$dir/$name').substitute(dir=path, name=file )


def succulent_part():
    sourceDir = input("\nEnter the source direcotory path: ")
    destDir   = input("\nEnter the destination direcotory path: ")
    extension_file = input("\nEnter the extension file (pess enter if you want move all): ")
    try:
        for f in listdir(sourceDir):
            if not extension_file:
                shutil.copy2(create_path(sourceDir,f), create_path(destDir,f))
            else:
                if fnmatch.fnmatch(f,'*'+extension_file):
                    shutil.copy2(create_path(sourceDir,f), create_path(destDir,f))

        if not extension_file:
            print(colored("\nAll files have been moved from ",'green') + colored(sourceDir, 'red', attrs=['bold']) 
                          + colored(" to ", 'green') + colored(destDir, 'red', attrs=['bold']))
        else:
            print(colored("\nAll files have been moved from ",'green') + colored(sourceDir, 'red', attrs=['bold']) 
                          + colored(" to ", 'green') + colored(destDir, 'red', attrs=['bold']) + colored(" and have extension " ,'green') + colored(extension_file, 'red', attrs=['bold']))
    except Exception as e: 
        print(e)


def clean_tha_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def show_menu():
    print(colored(pyfiglet.figlet_format("SPOSTA COSE.PY", font='slant'), 'red'))    
    print(colored("Sposta Cose.py is a simple utility that help you move file from folder to another.\nUsage:\nProvide the source directory path"+
    "and the destination directory path and the extension of file if you want move only the file that ends with for exaple with .txt",'green'))

def main():
    clean_tha_screen()
    show_menu()
    succulent_part()

if __name__ == "__main__":
    main()