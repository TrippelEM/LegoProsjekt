from pybricks.ev3devices import Motor

class Conveyor:
    
    moveSpeed = 0
    
    def __init__(self, motor):
        self.__motor = motor
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
