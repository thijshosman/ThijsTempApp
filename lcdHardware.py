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
        self.buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (0,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

        #create default color
        self.color=[1.0,1.0,1.0]

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
        if 'color' in kwargs:
            self.color=kwargs['color']
        self.lcd.set_color(self.color[0],self.color[1],self.color[2])
        if 'line1' in kwargs:
            self.line1 = kwargs['line1']
        if 'line2' in kwargs:
            self.line2 = kwargs['line2']
        self.lcd.message('{0}\n{1}'.format(self.line1,self.line2))

    def isButtonPressed(self):

        for button in self.buttons:
            if self.lcd.is_pressed(button[0]):
                #print "button %s pressed" % button[1]
                time.sleep(0.2)
                return button[1]
                #else:
                    #return False
