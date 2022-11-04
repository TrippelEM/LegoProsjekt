from pybricks.parameters import Port
from Conveyor import Conveyor
from Controller import Controller

class Player:
    
    startLives = 1
    
    def __init__(self, sensorPort, motorPort):
        self.__lives = Player.startLives
        self.__controller = Controller(sensorPort)
        self.__conveyor = Conveyor(motorPort)
        
        self.alive = True
        self.moving = False
    
    def update(self):
        self.__controller.update()
        
        if self.__controller.pressed:
            self.moving = True
            self.__conveyor.start()
        else:
            self.moving = False
            self.__conveyor.stop()
    
    def loseLife(self):
        self.__lives -= 1
        
        if self.__lives <= 0:
            self.alive = False
            self.__conveyor.gameOver()
        else:
            self.__conveyor.reset()