from pybricks.ev3devices import TouchSensor

class Controller:
    
    def __init__(self, sensor):
        self.__sensor = sensor
        self.pressed = False
        self.down = False
        self.up = False
        
    def update(self):
        
        self.down = False
        self.up = False
        
        if self.__sensor.pressed():
            if not self.pressed:
                self.down = True
            self.pressed = True
        else:
            if self.pressed:
                self.up = True
            self.pressed = False