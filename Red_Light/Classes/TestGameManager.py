from Classes.GameSettings import GameSettings
from Classes.Player import Player

class TestGameManager:
    
    def __init__(self, p1Sensor, p2Sensor, p1Motor, p2Motor):
        #self.head = Head()
        self.player1 = Player(p1Sensor, p1Motor)
        self.player2 = Player(p2Sensor, p2Motor)
    
    def startGame(self):
        print("Spillet starter")
        
    def updateGame(self):
        self.player1.update()
        self.player2.update()