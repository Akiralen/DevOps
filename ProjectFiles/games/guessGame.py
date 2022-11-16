import logging

from utils.utils import clear_screen
logging.basicConfig(
    format='%(asctime)s%(name)s%(levelname)s:%(message)s',
    datefmt='[%d.%m.%Y][%I:%M.%S]',
    level=logging.DEBUG,
    filename='event.log'
    )
import os
from random import randint
from utils.gameABC import games

        
class game(games):
    
    __dificulty = 0
    __result = False
    __secretNumber = 0
    __guess = -1
    
    def __init__(self):
        logging.debug("Object <guess game>")
    
    def __str__(self):
        return "Guess Game"
    
    def print_instructions(self):
        print(f"Your objective in this game to guess number between 1 and {self.__dificulty}\n--------------------")
        pass
   
    def print_result(self):
        print(f"The number was <{self.__secretNumber}>, your guess <{self.__guess}>ּּ.")
        if self.__result :
            print("You WIN!")
        else :
            print("You LOOSE!")
    
    def __generate_number(self):
        self.__secretNumber = randint(1,self.__dificulty)
        logging.debug(f'Set secret number as <{self.__secretNumber}>')
    
    def __get_guess(self):
        while not self.__guess-1 in range(self.__dificulty):
            clear_screen()
            try:
                self.__guess = int(input(f"Your guess [1-{self.__dificulty}]:"))
            except:
                self.__guess = -1
            logging.debug(f'Players guess: <{self.__guess}>')

    def __compare_result(self):
        if self.__guess == self.__secretNumber:
            self.__result = True
        else:
            self.__result = False
    
    def play(self,name):
        print(f"{name} welcome to 'Guess Game'")
        print(f"You have selected dificulty: {self.__dificulty}\n---------------------")
        self.print_instructions()
        os.system("pause")
        self.__generate_number()
        self.__get_guess()
        self.__compare_result()
        self.print_result()
        os.system("pause")
        
    def get_result(self) :
        return self.__result 
    def set_dificulty(self,dificulty):
        self.__dificulty = dificulty
        
def main():
    logging.info('Started module "guessGame.py" as stand alone')
    dificulty = 1
    g = game()
    name = 'Test'
    g.set_dificulty(dificulty)
    g.play(name)
    logging.info('Finished execution of module "guessGame.py"')
    
if __name__ == '__main__':
    #run game
    main()
else:
    logging.info('Module "guessGame.py" loaded')

    