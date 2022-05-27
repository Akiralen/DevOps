from distutils.log import INFO
import logging
import logging.config
logging.basicConfig(
    format='%(asctime)s%(levelname)s:%(message)s',
    datefmt='[%d.%m.%Y][%I:%M.%S]',
    level=INFO,
    filename='event.log'
    )

import live
import os

from misc import clear_screen

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
