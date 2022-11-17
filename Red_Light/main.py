#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Classes.GameSettings import GameSettings
from Classes.GameManager import GameManager
from Classes.AudioThread import AudioThread

# ---------- Create objects ---------- #
ev3 = EV3Brick()

# Robot
robSensor = TouchSensor(Port.S2)
robMotor = Motor(Port.C, Direction.CLOCKWISE)

# Player1
p1Sensor = TouchSensor(Port.S1)
p1Motor = Motor(Port.A, Direction.COUNTERCLOCKWISE) #gears=[10, 10]

# Player2
p2Sensor = TouchSensor(Port.S4)
p2Motor = Motor(Port.D, Direction.COUNTERCLOCKWISE) #gears=[10, 10]

# Litt usikker om skal være en class
settings = GameSettings(startLives=1, moveSpeed=30)
settings.applySettings()

# Game Manager
gameManager = GameManager(robSensor, robMotor, p1Sensor, p1Motor, p2Sensor, p2Motor)

# ---------- Game ---------- #
ev3.speaker.beep()

finished = False
while not finished:
    
    print("Menu")
    ev3.speaker.play_file("Audio/Start.wav")
    gameManager.startGame()
    
    # Game loop
    while True:
        gameManager.updateGame()
        
        if gameManager.winner != 0:
            break
    
    # Show winner
    if gameManager.winner == 3:
        print("Both won")
    elif gameManager.winner == 2:
        print("Player2 won")
    elif gameManager.winner == 1:
        print("Player1 won")
    else:
        print("Both died")
    
    gameManager.resetGame()
    wait(3000)
