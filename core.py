import shutil
import fnmatch
from string import Template
try:
    from termcolor import colored
except ImportError:
    raise ImportError('Please install termcolor launch this command pip or pip3 install termcolor')

from os import  name, listdir

def create_path(path, file):
    if name == 'nt':
        return Template('$dir\$name').substitute(dir=path, name=file )
    else:
         return Template('$dir/$name').substitute(dir=path, name=file )


def succulent_part():
    sourceDir = input("\nEnter the source directory path: ")
    destDir   = input("\nEnter the destination directory path: ")
    extension_file = input("\nEnter the extension file (press enter if you want to move all): ")
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