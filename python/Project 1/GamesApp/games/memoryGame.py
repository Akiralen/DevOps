
import logging

logging.basicConfig(
    format='%(asctime)s%(name)s%(levelname)s:%(message)s',
    datefmt='[%d.%m.%Y][%I:%M.%S]',
    level=logging.DEBUG,
    filename='event.log'
    )
import functools
import os
from time import sleep
from random import randint
from gameABC import games

def clear_screen():
    ### check OS and run correct command
    if (os.name == 'nt'): 
        os.system('cls')
    elif (os.name == 'posix'):
        os.system('clear')
        

class game(games):
    
    __dificulty = 0
    __result = False
    __sequence = []
    __guess = []
    
    def __init__(self):
        logging.debug("Object <memoryGame> instatiated")
    
    def __str__(self):
        return "Memory Game"
    
    def print_instructions(self):
        print(f"Your objective in this game to memorrise sequence of {self.__dificulty} numbers\n\
            You will be shown numbers afterward please enter sequence one by one")
   
    def print_result(self):
        print(f"The sequence was <{self.__sequence}>, your guess <{self.__guess}>ּּ.")
        if self.__result :
            print("You WIN!")
        else :
            print("You LOOSE!")
    
    def __generate_sequence(self):
        self.__sequence = []
        for i in range(self.__dificulty):
            self.__sequence.append(randint(1,101))
        logging.debug(f'Set secret number as <{self.__sequence}>')
        
    def __show_sequence(self):
        clear_screen()
        print("Get ready...")
        os.system("pause")
        for i in range(5):
            clear_screen()
            print(f"{5-i}...")
            sleep(1)
        for num in self.__sequence:
            clear_screen()
            print(f"<{num}>")
            sleep(0.7)
            
    
    def __get_list_from_user(self):
        for i in range(self.__dificulty):
            guess = -1
            while not (guess-1) in range(100):
                clear_screen()
                try:
                    guess = int(input(f"Number <{i+1}>:"))
                except:
                    guess = -1
            self.__guess.append(guess)
            logging.debug(f'Players guess: <{self.__guess}>')

    def __compare_result(self):
        if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,self.__sequence,self.__guess), True): 
           self.__result = True
        else:
            self.__result = False
    
    def play(self,name):
        print(f"{name} welcome to 'Memory Game'")
        print(f"You have selected dificulty: {self.__dificulty}")
        self.print_instructions()
        os.system("pause")
        self.__generate_sequence()
        self.__show_sequence()
        self.__get_list_from_user()
        self.__compare_result()
        self.print_result()
        os.system("pause")
        
    def get_result(self) :
        return self.__result 
    
    def set_dificulty(self,dificulty):
        self.__dificulty=dificulty
        
def main():
    logging.info('Started module "memoryGame.py" as stand alone')
    dificulty = 3
    g = game()
    name = 'Test'
    g.set_dificulty(dificulty)
    g.play(name)
    logging.info('Finished execution of module "memoryGame.py"')
    
if __name__ == '__main__':
    #run game
    main()
else:
    logging.info('Module "memoryGame.py" loaded')

    