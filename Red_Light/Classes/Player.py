from Classes.Controller import Controller
import time

class Player:
    
    startLives = 1
    moveSpeed = 30
    
    def __init__(self, sensor, motor):
        self.__controller = Controller(sensor)
        self.__motor = motor
        
        self.__lives = Player.startLives
        print(self.__lives)
        self.__moveSpeed = Player.moveSpeed
        
        self.alive = True
        self.moving = False
        self.canMove = True
        
        self.previousTime = 0
        self.waitTime = 0
    
    def start(self):
        self.previousTime = time.time()
    
    
    def update(self):
        self.__controller.update()
        
        currentTime = time.time()
        
        if self.canMove:
            if self.__controller.pressed():
                self.moving = True
                self.__motor.run(self.__moveSpeed)
            else:
                self.moving = False
                self.__motor.hold()
        else:
            self.moving = False
        
        if (currentTime - self.previousTime) >= self.waitTime:
            self.canMove = True
    
    
    def moveCheck(self):
        if self.canMove:
            if self.moving:
                self.__lives -= 1
                
                if self.__lives > 0:
                    self.reset()
                else:
                    self.die()
    
    def reset(self):
        self.canMove = False
        self.previousTime = time.time()
        self.waitTime = 2
        self.__motor.run(-60)
        
    def die(self):
        self.canMove = False
        self.previousTime = time.time()
        self.waitTime = 2
        self.__motor.run(-200)