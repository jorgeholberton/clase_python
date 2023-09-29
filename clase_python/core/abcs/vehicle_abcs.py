""" ABCs for Car Class. """

from abc import ABCMeta
from abc import abstractmethod

class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def move(self,distance_traveled:int)->None:
        pass
    
    @abstractmethod
    def doors(self,door_quantity:int)->None:
        pass 
    
    
    
        
    