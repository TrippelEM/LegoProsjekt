from pybricks.parameters import Port
from Classes.Player import Player
from Classes.Conveyor import Conveyor

class GameSettings:
    
    def __init__(self, startLives, moveSpeed):
        self.__startLives = startLives
        self.__moveSpeed = moveSpeed
        
    def applySettings(self):
        Player.startLives = self.__startLives
        Conveyor.moveSpeed = self.__moveSpeed