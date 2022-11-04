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
p1Motor = Motor(port = Port.A, positive_direction = Direction.COUNTERCLOCKWISE)
p2Motor = Motor(port = Port.D, positive_direction = Direction.COUNTERCLOCKWISE)

settings = GameSettings(startLives = 1, moveSpeed = 30)
gameManager = TestGameManager(p1Sensor, p2Sensor, p1Motor, p2Motor)

# Game
ev3.speaker.beep()
settings.applySettings()

while True:
    gameManager.updateGame()
