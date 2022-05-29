import logging
import os,imp

from games.misc import clear_screen


### Loading game objects from files in path to dictioanary
def load_library(path):
    gamesList = []

    ### get all items in directory
    with os.scandir(path) as dir :
        for item in dir :
            if item.is_file() :
                filepath=item.path
                mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
                ### try importing file as module
                failed = False
                if file_ext.lower() == '.py':
                    try:
                        py_mod = imp.load_source(mod_name, filepath)
                    except:
                        failed = True
                elif file_ext.lower() == '.pyc':
                    try:
                        py_mod = imp.load_compiled(mod_name, filepath)
                    except:
                        failed = True
                ### add new game class to list
                if not failed:
                    if hasattr(py_mod, 'game'):
                        class_inst = getattr(py_mod, 'game')()
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
    while not (dificulty-1) in range(5):
        try:
            dificulty = int(input('please select dificulty [1-5]:'))
        except:
            dificulty = -1
    return dificulty

def load_game(path,name):
    games=[]
    games = load_library(path)
    try:
        gamesCount = len(games)
    except:
        gamesCount = 0
    if gamesCount > 0:       
        wins = 0
        loses = 0
        
        selection = -1
        while not selection == 0:
            clear_screen()
            #print menu header
            print(f"Curent player <{name}>. Wins:{wins} | Loses:{loses}")
            #print games selection
            for i in range(gamesCount):
                print(f"{i+1}: {games[i]}")
            #print exit prompt
            print("----------------------")
            print("0:Exit")
            try:
                selection = int(input(f'Your choice, {name}:'))
                if selection in games:
                    pass
            except:
                selection = -1
            if (selection-1) in range(gamesCount):
                #run game
                dificulty = get_dificulty()
                logging.info(f'Starting game<{games[selection-1]}> at ({dificulty}) dificulty')
                games[selection-1].set_dificulty(dificulty)
                games[selection-1].play(name)
                logging.info(f"Game<{games[selection-1]}> at ({dificulty}) dificulty ended with <{('win' if games[selection-1].result else 'lose')}> result")
                if games[selection-1].get_result():
                    wins += 1
                else:
                    loses += 1
    else:
        logging.error("Unable to run. No games exist")
    
    
def welcome():
    name=input("Hi \n Please enter your name:")
    print(f"Hello {name} and welcome to the World of Games (WoG).\n\
        Here you can find many cool games to play.")
    os.system('pause')
    return name

if __name__ == '__main__':
    logging.error("This module can't be run as main")
else:
    logging.info('Module "live.py" loaded')
