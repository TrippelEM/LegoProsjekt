from pybricks.parameters import Port
from Player import Player
from Conveyor import Conveyor

class GameSettings:
    
    def __init__(self, startLives, moveSpeed):
        self.__startLives = startLives
        self.__moveSpeed = moveSpeed
        
    def applySettings(self):
        Player.startLives = self.__startLives
        Conveyor.moveSpeed = self.__moveSpeed