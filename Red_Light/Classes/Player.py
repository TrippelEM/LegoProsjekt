from pybricks.parameters import Stop
from Classes.AudioThread import AudioThread
import time

class Player:
    
    winAngle = 535
    deathAngle = -240
    
    startLives = 1
    moveSpeed = 30
    
    def __init__(self, sensor, motor):
        self.sensor = sensor
        self.motor = motor
    
    def start(self):
        self.lives = Player.startLives
        self.moveSpeed = Player.moveSpeed
        
        self.motor.reset_angle(0)
        self.moving = False
        self.canMove = False
        self.state = 0
    
    
    def update(self):
        
        if self.canMove:
            if self.sensor.pressed():
                self.moving = True
                self.motor.run(self.moveSpeed)
            else:
                self.moving = False
                self.motor.hold()
        else:
            self.moving = False
            
        if self.motor.angle() >= Player.winAngle:
            self.canMove = False
            self.state = 1
        elif self.motor.angle() <= Player.deathAngle:
            self.state = -2
    
    
    def loseLife(self):
        self.lives -= 1
        if self.lives > 0:
            self.reset()
        else:
            self.die()
        
    
    def reset(self):
        self.canMove = False
        self.motor.run_target(300, 0, then=Stop.HOLD, wait=False)
        
        
    def die(self):
        self.state = -1
        self.canMove = False
        self.motor.track_target(Player.deathAngle)
        AudioThread("Audio/Shot.wav", 0)