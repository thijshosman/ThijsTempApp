import time
import Adafruit_CharLCD as LCD

class LCDHardware(object):
    '''controls lcd hardware and reads out button output'''
    def __init__(self):

        self.lcd = LCD.Adafruit_CharLCDPlate()
        self.lcd.clear()
        self.lcd.message('initialized')
        self.line1 = ''
        self.line2 = ''

        # create some custom characters
        self.lcd.create_char(1, [2, 3, 2, 2, 14, 30, 12, 0])
        self.lcd.create_char(2, [0, 1, 3, 22, 28, 8, 0, 0])
        self.lcd.create_char(3, [0, 14, 21, 23, 17, 14, 0, 0])
        self.lcd.create_char(4, [31, 17, 10, 4, 10, 17, 31, 0])
        self.lcd.create_char(5, [8, 12, 10, 9, 10, 12, 8, 0])
        self.lcd.create_char(6, [2, 6, 10, 18, 10, 6, 2, 0])
        self.lcd.create_char(7, [31, 17, 21, 21, 21, 21, 17, 31])

        # Make list of button value, text, and backlight color.
        #self.buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
        #    (LCD.LEFT,   'Left'  , (1,0,0)),
        #    (LCD.UP,     'Up'    , (0,0,1)),
        #    (LCD.DOWN,   'Down'  , (0,1,0)),
        #    (LCD.RIGHT,  'Right' , (1,0,1)) )

        self.buttons = ( (LCD.SELECT, 'Select'),
            (LCD.LEFT,   'Left'),
            (LCD.UP,     'Up'  ),
            (LCD.DOWN,   'Down'),
            (LCD.RIGHT,  'Right') )

        #create default color
        #self.color=[1.0,1.0,1.0]

        # possible colors
        self.colorArray = ['red','green','blue','yellow','cyan','magenta','white']
        self.currentColorIndex = 0

    def setColor(self,color):
        '''set color to string value that translates into RGB vector'''
        if color == 'red':
            self.color = [1.0,0.0,0.0]
        elif color == 'green':
            self.color = [0.0,1.0,0.0]
        elif color == 'blue':
            self.color = [0.0,0.0,1.0]
        elif color == 'yellow':
            self.color = [1.0,1.0,0.0]
        elif color == 'cyan':
            self.color = [0.0,1.0,1.0]
        elif color == 'magenta':
            self.color = [1.0,0.0,0.0]
        elif color == 'white':
            self.color = [1.0,1.0,1.0]
        self.updateColor()

    def nextColor(self):
        '''cycle through colors'''
        self.currentColorIndex = (self.currentColorIndex + 1)%(len(self.colorArray))
        self.setColor(self.colorArray[self.currentColorIndex])
        return self.colorArray[self.currentColorIndex]

    def previousColor(self):
        '''cycle through colors'''
        self.currentColorIndex = (self.currentColorIndex - 1)%(len(self.colorArray))
        self.setColor(self.colorArray[self.currentColorIndex])
        return self.colorArray[self.currentColorIndex]

    def updateColor(self):
        '''tell the lcd hardware to change color'''
        self.lcd.set_color(self.color[0],self.color[1],self.color[2])
        #time.sleep(1)

        # # Show some basic colors.
        # lcd.set_color(1.0, 0.0, 0.0)
        # lcd.clear()
        # lcd.message('RED \x01')
        # time.sleep(3.0)

        # lcd.set_color(0.0, 1.0, 0.0)
        # lcd.clear()
        # lcd.message('GREEN \x02')
        # time.sleep(3.0)

        # lcd.set_color(0.0, 0.0, 1.0)
        # lcd.clear()
        # lcd.message('BLUE \x03')
        # time.sleep(3.0)

        # lcd.set_color(1.0, 1.0, 0.0)
        # lcd.clear()
        # lcd.message('YELLOW \x04')
        # time.sleep(3.0)

        # lcd.set_color(0.0, 1.0, 1.0)
        # lcd.clear()
        # lcd.message('CYAN \x05')
        # time.sleep(3.0)

        # lcd.set_color(1.0, 0.0, 1.0)
        # lcd.clear()
        # lcd.message('MAGENTA \x06')
        # time.sleep(3.0)

        # lcd.set_color(1.0, 1.0, 1.0)
        # lcd.clear()
        # lcd.message('WHITE \x07')
        # time.sleep(3.0)

    def update(self,*args,**kwargs):
        self.lcd.clear()
        if 'line1' in kwargs:
            self.line1 = kwargs['line1']
            self.lcd.message('{0}\n{1}'.format(self.line1,self.line2))
        if 'line2' in kwargs:
            self.line2 = kwargs['line2']
            self.lcd.message('{0}\n{1}'.format(self.line1,self.line2))

    def isButtonPressed(self):
        for button in self.buttons:
            if self.lcd.is_pressed(button[0]):
                #print "button %s pressed" % button[1]
                time.sleep(0.3)
                return button[1]

if __name__ == '__main__':
    lcd1 = LCDHardware()

    lcd1.update(line1='first line')
    lcd1.update(line2='second line')
    lcd1.setColor('red')
    lcd1.update(line1='updated first line')
    lcd1.nextColor()

