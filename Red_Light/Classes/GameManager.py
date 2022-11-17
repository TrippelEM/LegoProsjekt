from Classes.GameSettings import GameSettings 
from Classes.Player import Player
from Classes.Robot import Robot
import time, random

class GameManager:
    
    def __init__(self, robSensor, robMotor, p1Sensor, p1Motor, p2Sensor, p2Motor):
        self.robot = Robot(robSensor, robMotor)
        self.players = (Player(p1Sensor, p1Motor), Player(p2Sensor, p2Motor))
    
    def startGame(self):
        self.winner = 0
        self.robot.start()
        for player in self.players:
            player.start()

    def resetGame(self):
        self.robot.reset()
        for player in self.players:
            player.reset()
        
    def updateGame(self):
        
        # Update robot
        self.robot.update()
        
        # Update players
        for player in self.players:
            player.update()
        
        # Check if robot is looking
        if self.robot.looking:
            
            for player in self.players:
                if player.moving:
                    player.loseLife()
        
        
        for player in self.players:
            if player.state == 0 and self.robot.previousLooking and not self.robot.looking:
                player.canMove = True
            

        if self.players[0].state == 1 and self.players[1].state == 1:
            self.winner = 3
        elif self.players[1].state == 1:
            self.winner = 2
        elif self.players[0].state == 1:
            self.winner = 1
        elif self.players[0].state == -2 and self.players[1].state == -2:
            self.winner = -1