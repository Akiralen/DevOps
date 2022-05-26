from os import system
import os


def clearscreen():
    ### check OS and run correct command
    if (os.name == 'nt'): 
        os.system('cls')
    elif (os.name == 'posix'):
        os.system('clear')
            