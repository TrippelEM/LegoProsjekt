#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Classes.GameSettings import GameSettings
from Classes.GameManager import GameManager
from Classes.TestGameManager import TestGameManager

# Create objects
ev3 = EV3Brick()

p1Sensor = TouchSensor(Port.S1)
p2Sensor = TouchSensor(Port.S4)
robSensor = TouchSensor(Port.S2)

p1Motor = Motor(port=Port.A, positive_direction=Direction.COUNTERCLOCKWISE, gears=[10, 10])
p2Motor = Motor(port=Port.D, positive_direction=Direction.COUNTERCLOCKWISE, gears=[10, 10])
robMotor = Motor(port=Port.C, positive_direction=Direction.CLOCKWISE)

settings = GameSettings(startLives=2, moveSpeed=30)
settings.applySettings()

gameManager = GameManager(p1Sensor, p2Sensor, robSensor, p1Motor, p2Motor, robMotor)

# Game
ev3.speaker.beep()
gameManager.startGame()

while True:
    gameManager.updateGame()
