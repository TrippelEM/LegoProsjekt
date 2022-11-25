from pybricks.ev3devices import Motor
from pybricks.parameters import Stop
from Classes.AudioThread import AudioThread
import time, random

class Robot:
    
    turnSpeed = 300
    turnTime = 0.4
    
    def __init__(self, sensor, motor):
        self.sensor = sensor
        self.motor = motor
    
    def start(self):
        self.turnSpeed = Robot.turnSpeed
        self.turnTime = Robot.turnTime
        
        self.motor.reset_angle(0)
        self.turning = False
        self.looking = True
        
        self.previousLooking = True
        self.previousTime = time.time()
        self.waitTime = 0
    
    def update(self):
        
        # Get current time
        currentTime = time.time()
        
        if (currentTime - self.previousTime) >= self.waitTime:
            self.previousTime = time.time()
            
            if self.turning:
                self.turning = False
                if self.looking:
                    # Looking away
                    self.looking = False
                    self.waitTime = 5 + random.random() * 3
                    AudioThread("Audio/Counting.wav", 0)
                else:
                    # Looking towards
                    self.looking = True
                    self.waitTime = 3 + random.random() * 3
            else:
                self.turning = True
                if self.looking:
                    # Turning away
                    self.turning = True
                    self.motor.run_target(self.turnSpeed, 180, then=Stop.HOLD, wait=False)
                    self.waitTime = 0
                else:
                    # Turning towards
                    self.turning = True
                    if self.turnTime == 0:
                        self.motor.track_target(0)
                    else:
                        self.motor.run_target(self.turnSpeed, 0, then=Stop.HOLD, wait=False)
                    self.waitTime = self.turnTime
    
    def reset(self):
        self.motor.run_target(300, 0, then=Stop.HOLD, wait=False)