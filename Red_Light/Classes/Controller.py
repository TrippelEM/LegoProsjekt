from pybricks.ev3devices import TouchSensor

class Controller:
    
    def __init__(self, sensor):
        self.__sensor = sensor
        self.__pressed = False
        self.__down = False
        self.__up = False
        
    def update(self):
        self.__down = False
        self.__up = False
            
        if self.__sensor.pressed():
            if not self.__pressed:
                self.__down = True
            self.__pressed = True
        else:
            if self.__pressed:
                self.up = True
            self.__pressed = False
    
    def pressed(self):
        return self.__pressed
    
    def down(self):
        return self.__down
    
    def up(self):
        return self.__up