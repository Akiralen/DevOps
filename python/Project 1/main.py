from distutils.debug import DEBUG
import logging
import logging.config
# logging.basicConfig(
#     format='%(asctime)s%(levelname)s:%(message)s',
#     datefmt='[%d.%m.%Y][%I:%M.%S]',
#     level=DEBUG
#     )
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('file')

import live
import os

from misc import clearscreen

### Loading game objects in dictioanary

def main():
    logger.info('Program started')
    clearscreen()
    gamePath = os.path.abspath('./games')
    playername = live.welcome()
    live.load_game(gamePath,playername)
    logger.info('Program ended.')
if __name__ == "__main__":
    main()
else:
    logger.error("This is not a module")
