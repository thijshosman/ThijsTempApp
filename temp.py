
class tempSensor:

    def __init__(self,pin=4):
        import Adafruit_DHT
        self.sensor = Adafruit_DHT.AM2302
        self.DHT = Adafruit_DHT
        self.pin=pin
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        print humidity,temperature

    def read(self):
        humidity, temperature = self.DHT.read_retry(self.sensor, self.pin)
        return humidity, temperature

if __name__ == '__main__':
    aSensor = tempSensor()
    aSensor.read()


