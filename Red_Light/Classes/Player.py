from Classes.Controller import Controller
from Classes.Conveyor import Conveyor

class Player:
    
    startLives = 1
    
    def __init__(self, sensor, motor):
        self.__lives = Player.startLives
        self.__controller = Controller(sensor)
        self.__conveyor = Conveyor(motor)
        
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