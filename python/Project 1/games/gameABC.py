# Abstract method for games

from abc import ABC, abstractmethod, abstractproperty


class games(ABC):
    @property
    def dificulty(self) :
        pass
    @property
    def result(self) :
        pass
    
    @abstractmethod
    def __init__(self) :
        pass
    @abstractmethod
    def __str__(self) :
        pass
    @abstractmethod
    def play(self) :
        pass
    @abstractmethod
    def printresult(self) :
        pass
    
    def getresult(self) :
        return self.result    
    def setdificulty(self,dificulty):
        self.dificulty=dificulty