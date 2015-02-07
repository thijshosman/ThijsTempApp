
from observer import *

import Adafruit_DHT


class tempSensor(Observable):

    def __init__(self,pin=4):
        self.sensor = Adafruit_DHT.AM2302
        self.DHT = Adafruit_DHT
        self.pin=pin
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        print humidity,temperature

    def read(self):
        humidity, temperature = self.DHT.read_retry(self.sensor, self.pin)
        self.broadcast(humidity=humidity,temperature=temperature)
        return humidity, temperature

    def broadcast(self):
        self.notify_observers(*args,**kwargs)

if __name__ == '__main__':
    aSensor = tempSensor()
    aSensor.read()


