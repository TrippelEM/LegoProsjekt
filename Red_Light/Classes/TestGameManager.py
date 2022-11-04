from GameSettings import GameSettings
from Player import Player

class GameManager:
    
    def __init__(self, p1SensorPort, p2SensorPort, p1MotorPort, p2MotorPort):
        self.player1 = Player(p1SensorPort, p1MotorPort)
        self.player2 = Player(p2SensorPort, p2MotorPort)
    
    def startGame(self):
        print("Spillet starter")
        
    def updateGame(self):
        self.player1.update()
        self.player2.update()