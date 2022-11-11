from pybricks.ev3devices import Motor
from pybricks.parameters import Stop
import time, random

class Robot:
    
    turnSpeed = 300
    
    def __init__(self, motor):
        self.__motor = motor
        self.__motor.reset_angle(0)
        self.__looking = True
        self.__turning = False
        
        self.__turnSpeed = Robot.turnSpeed
        self.__turnTime = 0.5
        
        self.__previousTime = 0
        self.__waitTime = 0
    
    def start(self):
        self.previousTime = time.time()
    
    def update(self):
        currentTime = time.time()
        
        if (currentTime - self.__previousTime) >= self.__waitTime:
            self.__previousTime = time.time()
            
            if self.__looking:
                if self.__turning:
                    self.__turning = False
                    self.__waitTime = 5
                else:
                    self.__turning = True
                    self.__looking = False
                    self.__motor.run_target(self.__turnSpeed, 180, then=Stop.HOLD, wait=False)
            else:
                if self.__turning:
                    self.__turning = False
                    self.__waitTime = 5
                else:
                    self.__turning = True
                    self.__looking = True
                    self.__motor.run_target(self.__turnSpeed, 0, then=Stop.HOLD, wait=False)
                    self.__waitTime = self.__turnTime
            
        
    def looking(self):
        return self.__looking