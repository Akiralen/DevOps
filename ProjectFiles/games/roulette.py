import logging

from utils import clear_screen
logging.basicConfig(
    format='%(asctime)s%(name)s%(levelname)s:%(message)s',
    datefmt='[%d.%m.%Y][%I:%M.%S]',
    level=logging.DEBUG,
    filename='event.log'
    )
import os
import json
import urllib.request
from random import randint
from gameABC import games

        
class game(games):
    
    __dificulty = 0
    __result = False
    __curencyAmount = 0
    __range = []
    __guess = 0.0
    
    def __init__(self):
        logging.debug("Object <roulete> instatiated")
    
    def __str__(self):
        return "Curency Roulette"
    
    def print_instructions(self):
        print(f"Your objective in this game to guess conversion of curency from USD to ILS\n\
            To win you have to guess within range of +/- {5-self.__dificulty}")
        pass
   
    def print_result(self):
        print(f"Your guess was<{self.__guess}>ּּ, your answer was suposed to be in range [{self.__range[0]}-{self.__range[1]}]")
        if self.__result :
            print("You WIN!")
        else :
            print("You LOOSE!")
    
    def __generate_curency_ammount(self):
        self.__curencyAmount = randint(1,100)
        logging.debug(f'Set curency ammout set as <{self.__curencyAmount}>')
    
    def __get_exchange_rate(self):
        try:
            # making GET request to server and parsing data as JSON
            url = 'https://v6.exchangerate-api.com/v6/17f2ba5a3f8f83a07d140bb8/latest/USD'
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode('utf-8'))
            # returning conversion rate for USD to ILS
            rate = data.get("conversion_rates").get("ILS")
            logging.info(f"retrieved conversion rate USD-ILS<{rate}>")
            return rate
        except:
            logging.error("Unable to retrieve exchange rate")
   
    def __set_money_interval(self):
        totalvalue = self.__get_exchange_rate() * self.__curencyAmount
        self.__range = [totalvalue - (5 - self.__dificulty),totalvalue + (5 - self.__dificulty)]
    
    def __get_guess(self):
        success = False
        while not success:
            clear_screen()
            try:
                self.__guess = float(input(f"Your guess for conversion of {self.__curencyAmount}$:"))
                success = True
            except:
                success = False
            logging.debug(f'Players guess: <{self.__guess}>')

    def __compare_result(self):
        if self.__range[0] < self.__guess < self.__range[1]:
            self.__result = True
        else:
            self.__result = False
    
    def play(self,name):
        print(f"{name} welcome to 'Currency Roulette'")
        print(f"You have selected dificulty: {self.__dificulty}")
        self.print_instructions()
        os.system("pause")
        self.__generate_curency_ammount()
        self.__set_money_interval()
        self.__get_guess()
        self.__compare_result()
        self.print_result()
        os.system("pause")

    def get_result(self) :
        return self.__result 
    
    def set_dificulty(self,dificulty):
        self.__dificulty = dificulty

def main():
    logging.info('Started module "roulette.py" as stand alone')
    dificulty = 1
    g = game()
    name = 'Test'
    g.set_dificulty(dificulty)
    g.play(name)
    logging.info('Finished execution of module "roulette.py"')
    
if __name__ == '__main__':
    #run game
    main()
else:
    logging.info('Module "roulete.py" loaded')

    