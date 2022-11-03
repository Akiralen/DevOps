import logging
import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 999

def clear_screen():
    ### check OS and run correct command
    if (os.name == 'nt'): 
        os.system('cls')
    elif (os.name == 'posix'):
        os.system('clear')


if __name__ == '__main__':
    logging.error("This module can't be run as main")
else:
    logging.info('Module "live.py" loaded')