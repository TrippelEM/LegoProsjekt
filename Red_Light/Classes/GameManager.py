from Classes.GameSettings import GameSettings 
from Classes.Player import Player
from Classes.Robot import Robot
import time, random

class GameManager:
    
    def __init__(self, p1Sensor, p2Sensor, p1Motor, p2Motor, robMotor):
        self.player1 = Player(p1Sensor, p1Motor)
        self.player2 = Player(p2Sensor, p2Motor)
        self.robot = Robot(robMotor)
        
        self.previousTime = 0
        self.waitTime = 0
    
    def startGame(self):
        #Start og snu hode
        #Begynn å telle
        #Set wait time til random
        #Gjør det mulig for spillere å bevege seg        
        print("Starting game")
        self.previousTime = time.time()
        self.waitTime = 5
        self.robot.start()
        self.player1.start()
        self.player2.start()
        
    def updateGame(self):
        
        #Set variabler
        currentTime = time.time()
        
        #Spillere
        self.player1.update()
        self.player2.update()
        
        if self.robot.looking():
            self.player1.moveCheck()
            self.player2.moveCheck()
        
        #Robot
        self.robot.update()
            
    
    def resetGame(self):
        print("Reset")