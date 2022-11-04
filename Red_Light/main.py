from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Classes import GameSettings, GameManager, TestGameManager

# Set ports
p1SensorPort = Port.A
p2SensorPort = Port.B

p1MotorPort = Port.C
p2MotorPort = Port.D


# Create objects
ev3 = EV3Brick()
settings = GameSettings(startlives = 1, moveSpeed = 10)
gameManager = TestGameManager(p1SensorPort, p2SensorPort, p1MotorPort, p2MotorPort)

# Game
ev3.speaker.beep()

while True:
    gameManager.updateGame()
