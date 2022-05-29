import logging
logging.basicConfig(
    format='%(asctime)s<%(name)s>%(levelname)s:%(message)s',
    datefmt='[%d.%m.%Y|%I:%M.%S]',
    level=logging.INFO,
    filename='event.log'
    )

import live
import os

def clear_screen():
    ### check OS and run correct command
    if (os.name == 'nt'): 
        os.system('cls')
    elif (os.name == 'posix'):
        os.system('clear')
        
### Loading game objects in dictioanary

def main():
    logging.info('Program started')
    clear_screen()
    gamePath = os.path.abspath('./games')
    playername = live.welcome()
    live.load_game(gamePath,playername)
    logging.info('Program ended.')
if __name__ == "__main__":
    main()
else:
    logging.error("This is not a module")
