# Abstract method for games modules

from abc import ABC, abstractmethod
import logging


class games(ABC):
    @property
    #games dificulty
    def __dificulty(self) :
        pass
    @property
    #Success or failure of the game
    def __result(self) :
        pass
    
    @abstractmethod
    def __init__(self) :
        pass
    @abstractmethod
    #Returns game description when converted to string
    def __str__(self) :
        pass
    @abstractmethod
    #Prints result of a game
    def print_result(self) :
        pass
    @abstractmethod
    #main game body recieves player name
    def play(self,name) :
        pass
    
    @abstractmethod
    #Prints game instruction
    def print_instructions(self):
        pass
    
    @abstractmethod
    #returns result     
    def get_result(self) :
        pass
    @abstractmethod  
    #sets game difficulty 
    def set_dificulty(self,dificulty):
        pass
        
if __name__ == '__main__':
    logging.error("This module can't be run as main")
else:
    logging.info('Module "gamesABC.py" loaded')
