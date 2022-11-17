from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import SoundFile
import threading, time

class AudioThread:
    
    def __init__(self, soundFile, waitTime):
        self.thread = threading.Thread(target=self.playAudioFile, args=[soundFile, waitTime])
        self.thread.start()
        
    def playAudioFile(self, soundFile, waitTime):
        time.sleep(waitTime)
        ev3 = EV3Brick()
        ev3.speaker.play_file(soundFile)