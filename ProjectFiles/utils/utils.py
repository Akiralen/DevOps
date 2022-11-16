import logging
import os

SCORES_FILE_NAME = "./scores/scores.txt"
BAD_RETURN_CODE = 999


def clear_screen():
    ### check OS and run correct command
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

def wait_anykey():
    if os.name == "nt":
        os.system("pause")
    elif os.name == "posix":
        os.system('read -p "Press any key to continue"')

if __name__ == "__main__":
    logging.error("This module can't be run as main")
else:
    logging.info('Module "live.py" loaded')
