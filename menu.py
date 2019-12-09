try:
    import pyfiglet
except ImportError:
    raise ImportError('Please install pyfiglet launch this command pip or pip3 install pyfiglet')


try:
    from termcolor import colored
except ImportError:
    raise ImportError('Please install termcolor launch this command pip or pip3 install termcolor')

def show_menu():
    print(colored(pyfiglet.figlet_format("SPOSTA COSE.PY", font='slant'), 'red'))    
    print(colored("Sposta Cose.py is a simple utility that helps you tomove file from folder to another.\nUsage:\nProvide the source directory path"+
    "and the destination directory path and the extension of file if you want to move only the file that ends with for example .txt",'green'))