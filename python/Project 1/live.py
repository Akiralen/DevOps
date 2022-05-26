import logging
import os,imp


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
                        try:
                            class_inst = getattr(py_mod, 'game')()
                            gamesList.append(class_inst)
                            logging.info(f"Loading {class_inst} at index {len(gamesList)}")
                        except:
                            pass
    print(len(gamesList))
    if len(gamesList) < 1:
        logging.error("No games were loaded")
    else:
        logging.info(f"({len(gamesList)}) games loaded")
        return gamesList
                
def load_game(path,name):
    games=[]
    games = load_library(path)
    if len(games) < 1:        
        wins = 0
        looses = 0
        selection = -1
        while not selection == 0:
            for game,i in games:
                print(f"{i+1}: {game}")
            print("----------------------")
            print("0:Exit")
            try:
                selection = int(input(f'Your choice {name}:'))
                if selection in games:
                    pass
            except:
                pass
            selection = 0
    else:
        logging.error("Unable to run. No games exist")
    
    
def welcome():
    name=input("Hi \n Please enter your name:")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    return name

if __name__ == '__main__':
    logging.error("This module can't be run as main")
else:
    #logging.info('Module "live.py" loaded')
    pass