#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from Classes.GameManager import GameManager
from Classes.Gamemode import Gamemode
from Classes.AudioThread import AudioThread


# ---------- Objects ---------- #

ev3 = EV3Brick()

# Robot
robSensor = TouchSensor(Port.S2)
robMotor = Motor(Port.C, Direction.CLOCKWISE)

# Player1
p1Sensor = TouchSensor(Port.S1)
p1Motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

# Player2
p2Sensor = TouchSensor(Port.S4)
p2Motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# Game Manager
gameManager = GameManager(robSensor, robMotor, p1Sensor, p1Motor, p2Sensor, p2Motor)

# Gamemodes
gamemodes = []
gamemodes.append(Gamemode(name="Easy", turnSpeed=250, turnTime=0.7, startLives=3, moveSpeed=20))
gamemodes.append(Gamemode(name="Normal", turnSpeed=500, turnTime=0.4, startLives=3, moveSpeed=20))
gamemodes.append(Gamemode(name="Hard", turnSpeed=999, turnTime=0, startLives=3, moveSpeed=20))
gamemodes.append(Gamemode(name="Hardcore", turnSpeed=999, turnTime=0, startLives=1, moveSpeed=20))


# ---------- Methods ---------- #

def updateInput(sensor, pressed, index):
    if sensor.pressed():
        previousPressed = pressed[index]
        pressed[index] = True
        
        if not previousPressed:
            return True
        else:
            return False
            
    else:
        pressed[index] = False
        return False

def showMenu(option, options):
    ev3.screen.clear()
    
    step = ev3.screen.height / len(options)
    font = Font("Lucida", int(step) - 16)
    ev3.screen.set_font(font)
    
    for i in range(len(options)):
        boxCoord1 = (0, step * i)
        boxCoord2 = (ev3.screen.width, step * i + step)
        textCoord = ((boxCoord1[0] + boxCoord2[0]) / 2 - font.text_width(options[i]) / 2, (boxCoord1[1] + boxCoord2[1]) / 2 - font.height / 2)
        
        boxColor = Color.BLACK if i == option else Color.WHITE
        textColor = Color.WHITE if i == option else Color.BLACK
        
        ev3.screen.draw_box(boxCoord1[0], boxCoord1[1], boxCoord2[0], boxCoord2[1], r=0, fill=True, color=boxColor)
        ev3.screen.draw_text(textCoord[0], textCoord[1], options[i], text_color=textColor)

def updateMenu(pressed, option, options):
    input = []
    input.append(updateInput(robSensor, pressed, 0))
    input.append(updateInput(p1Sensor, pressed, 1))
    input.append(updateInput(p2Sensor, pressed, 2))
        
    if input[0]:
        return True
    elif input[1] or input[2]:
        option[0] += 1
        if option[0] >= len(options):
            option[0] = 0
        showMenu(option[0], options)
    return False

def showResult(text, size):
    ev3.screen.clear()
    
    font = Font("Lucida", size)
    ev3.screen.set_font(font)
    
    ev3.screen.draw_box(0, 0, ev3.screen.width, ev3.screen.height, r=0, fill=True, color=Color.WHITE)
    ev3.screen.draw_text((ev3.screen.width / 2) - (font.text_width(text) / 2), (ev3.screen.height / 2) - (font.height / 2), text, text_color=Color.BLACK)
        

# ---------- Program ---------- #

ev3.speaker.beep()

menuOption = [0]
menuOptions = ["Play", "Gamemode", "Exit"]

gamemodeOption = [1]
gamemodeOptions = []
for gamemode in gamemodes:
    gamemodeOptions.append(gamemode.name)

finished = False
while not finished:
    
    # Menu loop
    showMenu(menuOption[0], menuOptions)
    main = True
    
    pressed = [False, False, False]
    while True:
        if main:
            selected = updateMenu(pressed, menuOption, menuOptions)
            if selected:
                if menuOption[0] == 0:
                    gamemodes[gamemodeOption[0]].apply()
                    break
                elif menuOption[0] == 1:
                    main = False
                    menuOption[0] = 0
                    showMenu(gamemodeOption[0], gamemodeOptions)
                else:
                    finished = True
                    break
        else:
            selected = updateMenu(pressed, gamemodeOption, gamemodeOptions)
            if selected:
                main = True
                showMenu(menuOption[0], menuOptions)
    
    # Start game
    if finished:
        break
    ev3.screen.clear()
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
        showResult("Both won", 32)
    elif gameManager.winner == 2:
        print("Player 2 won")
        showResult("Player 2 won", 22)
    elif gameManager.winner == 1:
        print("Player 1 won")
        showResult("Player 1 won", 22)
    else:
        print("Both died")
        showResult("Both died", 32)
    
    gameManager.resetGame()
    wait(3000)
    
    # Wait for input
    pressed = [True, True, True]
    while True:
        input = []
        input.append(updateInput(robSensor, pressed, 0))
        input.append(updateInput(p1Sensor, pressed, 1))
        input.append(updateInput(p2Sensor, pressed, 2))
        
        if input[0]:
            break
        
showResult("Thanks for playing!", 18)
wait(2500)