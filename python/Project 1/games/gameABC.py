# Abstract method for games

from abc import ABC, abstractmethod
import logging


class games(ABC):
    @property
    def __dificulty(self) :
        pass
    @property
    def __result(self) :
        pass
    
    @abstractmethod
    def __init__(self) :
        pass
    @abstractmethod
    def __str__(self) :
        pass
    @abstractmethod
    def print_result(self) :
        pass
    @abstractmethod
    def play(self,name) :
        pass
    
    @abstractmethod
    def print_instructions(self):
        pass
    
    @abstractmethod    
    def get_result(self) :
        pass
    @abstractmethod   
    def set_dificulty(self,dificulty):
        pass
        
if __name__ == '__main__':
    logging.error("This module can't be run as main")
else:
    logging.info('Module "gamesABC.py" loaded')
