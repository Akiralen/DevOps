import logging
logging.basicConfig(
    format='%(asctime)s%(name)s%(levelname)s:%(message)s',
    datefmt='[%d.%m.%Y][%I:%M.%S]',
    level=logging.DEBUG,
    filename='event.log'
    )
import os
from misc import clear_screen
from random import randint
from gameABC import games


class game(games):
    
    __dificulty = 0
    __result = False
    __sequence = []
    __guess = []
    
    def __init__(self,dificulty : int):
        self.__dificulty = dificulty
        logging.debug(f"Object instatiated with dificulty <{self.__dificulty}>")
    
    def __str__(self):
        return "Memory Game"
    
    def print_instructions(self):
        print(f"Your objective in this game to guess number between 1 and {self.__dificulty}")
        pass
   
    def print_result(self):
        print(f"The number was <{self.__secretNumber}>, your guess <{self.__guess}>ּּ.")
        if self.__result :
            print("You WIN!")
        else :
            print("You LOOSE!")
    
    def __generate_sequence(self):
        self.__sequence = []
        for i in range(self.__dificulty):
            self.__sequence.append(randint(1,101))
        logging.debug(f'Set secret number as <{self.__sequence}>')
    
    def __get_guess(self):
        while not self.__guess-1 in range(100) + 1:
            clear_screen()
            try:
                self.__guess = int(input("Your guess:"))
            except:
                self.__guess = -1
            logging.debug(f'Players guess: <{self.__guess}>')

    def __compare_result(self):
        if self.__guess == self.__secretNumber:
            self.__result = True
        else:
            self.__result = False
    
    def play(self,name):
        print(f"{name} welcome to 'Memory Game'")
        print(f"You have selected dificulty: {self.__dificulty}")
        self.print_instructions()
        os.system("pause")
        self.__generate_sequence()
        self.__get_guess()
        self.__compare_result()
        self.print_result()
        os.system("pause")
        
def main():
    logging.info('Started module "memoryGame.py" as stand alone')
    dificulty = 1
    g = game(dificulty)
    name = 'Test'
    g.set_dificulty(dificulty)
    g.play(name)
    logging.info('Finished execution of module "memoryGame.py"')
    
if __name__ == '__main__':
    #run game
    main()
else:
    logging.info('Module "memoryGame.py" loaded')

    