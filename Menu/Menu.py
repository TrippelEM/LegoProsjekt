from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


from pybricks.ev3dev2.display import Display #kanskje noe feil med importeringen av display
import time, sleep
from ev3dev.ev3 import *
import os
os.systemos.system('setfont Lat15-TerminusBold14') #kanskje noe feil her åg

class Menu:
    option1 = "1. play a game"
    option2 = "2. bla bla"
    option3 = "exit"
    lcd = Display()
    options = [option1, option2, option3]
    x = len(options)
    choiceButton = TouchSensor(port = Port.S2)
    #178x128
    
    def __init__(self)
        self.__buttonStatus = False
        self.__buttonHold = False
      
      
    #programmet vil først vise full meny og forklaring på navigasjon, derretter vise en og en option ettersom knappen trykkes inn. 
    #om den holdes inne når den er inne på en option, utføres gitt oppgave
    def showScreen():
            
            print("---MENU---")
            print("Press button to scroll through")
            print(options[0])
            print(options[1])
            print(options[2])
            
            for x in options:
                if __buttonStatus = True:
                    print(x)
                    if __buttonHold = True: #kankskje må defineres som egen metode, skjekke gitt tid har gått.
                        #do execution of menu option, bruk index
            
            
            
        
        
        
        
