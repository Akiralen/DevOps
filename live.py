import logging
import os, imp
import utils.score as score
from utils.utils import clear_screen, wait_anykey

### Loading game objects from files in path to dictioanary
def load_library(path):
    gamesList = []

    ### get all items in directory
    with os.scandir(path) as dir:
        for item in dir:
            if item.is_file():
                filepath = item.path
                mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])
                ### try importing file as module
                failed = False
                if file_ext.lower() == ".py":
                    try:
                        py_mod = imp.load_source(mod_name, filepath)
                    except Exception as e:
                        failed = True
                        print(e)
                elif file_ext.lower() == ".pyc":
                    try:
                        py_mod = imp.load_compiled(mod_name, filepath)
                    except:
                        failed = True
                ### add new game class to list
                if not failed:
                    if hasattr(py_mod, "game"):
                        class_inst = getattr(py_mod, "game")()
                        gamesList.append(class_inst)
                        logging.info(f"Loading {class_inst} at index {len(gamesList)}")

    if len(gamesList) < 1:
        logging.warning(f"No games were loaded ({len(gamesList)})")
    else:
        logging.info(f"({len(gamesList)}) games loaded")
        return gamesList


def get_dificulty():
    clear_screen()
    dificulty = -1
    while not (dificulty - 1) in range(5):
        try:
            dificulty = int(input("please select dificulty [1-5]:"))
        except:
            dificulty = -1
    return dificulty


def load_game(path, name):
    games = []
    games = load_library(path)
    try:
        gamesCount = len(games)
    except:
        gamesCount = 0
    if gamesCount > 0:
        curent_score = score.read_scores().get(name, 0)

        selection = -1
        while not selection == 0:
            clear_screen()
            # print menu header
            print(f"Curent player <{name}>. Score:{curent_score}")
            # print games selection
            for i in range(gamesCount):
                print(f"{i+1}: {games[i]}")
            # print exit prompt
            print("----------------------")
            print("0:Exit")
            try:
                selection = int(input(f"Your choice, {name}:"))
                if selection in games:
                    pass
            except:
                selection = -1
            if (selection - 1) in range(gamesCount):
                # run game
                dificulty = get_dificulty()
                logging.info(
                    f"Starting game<{games[selection-1]}> at ({dificulty}) dificulty"
                )
                games[selection - 1].set_dificulty(dificulty)
                games[selection - 1].play(name)
                logging.info(
                    f"Game<{games[selection-1]}> at ({dificulty}) dificulty ended with <{('win' if games[selection-1].get_result() else 'lose')}> result"
                )
                if games[selection - 1].get_result():
                    win_score = (dificulty * 5) + 5
                    score.add_score(name, win_score)
                    curent_score = +win_score

    else:
        logging.error("Unable to run. No games exist")


def welcome():
    name = input("Hi, please enter your name:")
    clear_screen()
    print(
        f"Hello {name} and welcome to the World of Games (WoG).\n\
        Here you can find many cool games to play."
    )
    wait_anykey()
    return name


if __name__ == "__main__":
    logging.error("This module can't be run as main")
else:
    logging.info("Module" + __name__ + "loaded")
