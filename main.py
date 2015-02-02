
from lcd import *
from temp import *
#import observer
import time


# create lcd screen
lcd1 = lcdscreen()
lcd1.start()

aSensor = tempSensor()
print aSensor.read()


while True:
    humidity,temperature = aSensor.read()
    print temperature
    lcd1.update(temperature)
    time.sleep(3.0)





