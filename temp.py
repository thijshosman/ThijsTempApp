
from observer import *
import Adafruit_DHT
import time
import threading

class tempSensor():

    def __init__(self,pin=4):
        self.sensor = Adafruit_DHT.AM2302
        self.DHT = Adafruit_DHT
        self.pin=pin
        # humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        # print humidity,temperature

    def readTemp(self):
        humidity, temperature = self.DHT.read_retry(self.sensor, self.pin)
        return temperature

    # def broadcast(self,*args,**kwargs):
    #    self.notify_observers(*args,**kwargs)

class sensorPoller(threading.Thread):
    '''temporarily polls the temperature sensor'''
    def __init__(self,sensor,interval=2):
        self.sensor = sensor
        self.observable = Observable()
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        self.interval = interval

    def broadcast(self,*args,**kwargs):
        self.observable.notify_observers(*args,**kwargs)

    def run(self):
        while self.stop_event.is_set() == False:
            # print self.sensor.readTemp()
            temperature = self.sensor.readTemp()
            self.broadcast(temperature = temperature)
            time.sleep(self.interval)

    def stop(self):
        self.stop_event.set()

if __name__ == '__main__':

    aSensor = tempSensor()

    aTempPoller = sensorPoller(aSensor,interval=2)

    #register default observer with the poller
    firstobserver = Observer(aTempPoller.observable)

    aTempPoller.start()

    do_exit = False
    while do_exit == False:
        try:
            # sleep some time
            time.sleep(0.1)
        except KeyboardInterrupt:
            # Ctrl+C was hit - exit program
            do_exit = True

        # stop all running thread
    aTempPoller.stop()

