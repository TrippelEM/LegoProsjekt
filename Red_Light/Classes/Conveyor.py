from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction

class Conveyor:
    
    moveSpeed = 10
    
    def __init__(self, motorPort):
        self.__motor = Motor(port=motorPort, positive_direction=Direction.CLOCKWISE)
        self.__motor.reset_angle(0)
        self.__angle = 0
    
    def start(self):
        self.__motor.run(Conveyor.moveSpeed)
        
    def stop(self):
        self.__motor.stop()
        #self.__motor.brake()
        #self.__motor.hold()
    
    def reset(self):
        self.__motor.run(-100)
    
    def gameOver(self):
        self.__motor.run(-100)
