from Classes.Robot import Robot
from Classes.Player import Player

class Gamemode:
    def __init__(self, name, turnSpeed, turnTime, startLives, moveSpeed):
        self.name = name
        self.turnSpeed = turnSpeed
        self.turnTime = turnTime
        self.startLives = startLives
        self.moveSpeed = moveSpeed
        
    def apply(self):
        Robot.turnSpeed = self.turnSpeed
        Robot.turnTime = self.turnTime
        Player.startLives = self.startLives
        Player.moveSpeed = self.moveSpeed