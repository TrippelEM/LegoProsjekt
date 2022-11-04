from Classes.GameSettings import GameSettings 
from Classes.Player import Player
import time, random

class GameManager:
    
    def __init__(self, p1Sensor, p2Sensor, p1Motor, p2Motor):
        #self.head = Head()
        self.player1 = Player(p1Sensor, p1Motor)
        self.player2 = Player(p2Sensor, p2Motor)
        
        self.previousTime = 0
        self.waitTime = 0
    
    def startGame(self):
        #Start og snu hode
        #Begynn å telle
        #Set wait time til random
        #Gjør det mulig for spillere å bevege seg
        print("Start")
        
    def updateGame(self):
        
        #Set variabler
        currentTime = time.time()
        
        #Hode
        if currentTime - self.previousTime >= self.waitTime:
            print("Hmm")
            #Test om hodet er snudd eller ikke
            #Hvis ja
                #Snu hodet tilbake
                #Set waitTime til tilfeldig verdi
            #Hvis nei
                #Snu hodet bort
                #Set waitTime til tilfeldig verdi
            #if self.head
        
        #Oppdatter spillere
        self.player1.update()
        self.player2.update()
        
        #Sjekk om spiller 
        
        #Sjekk om spillere er døde eller i mål
    
    def resetGame(self):
        print("Reset")