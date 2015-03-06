
from lcd import *
from temp import *
#import observer
import time


# create lcd screen
lcd1 = lcdscreen(1,"test")
lcd1.start()



aSensor = tempSensor()
print aSensor.read()


while True:
    humidity,temperature = aSensor.read()

    formattedTemperature = "%.1f" % temperature

    print formattedTemperature
    lcd1.update(formattedTemperature)
    time.sleep(2.0)





