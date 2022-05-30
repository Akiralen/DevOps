import logging
from games.myutils import clear_screen
logging.basicConfig(
    format='%(asctime)s<%(name)s>%(levelname)s:%(message)s',
    datefmt='[%d.%m.%Y|%I:%M.%S]',
    level=logging.INFO,
    filename='event.log'
    )

import live
import os

      
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
