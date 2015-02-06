
import threading
import time
import math
from observer import *

class LCDDisplayUpdater(threading.Thread):
    #deprecated
    def __init__(self,lcd):

        threading.Thread.__init__(self)

        self.threadLock = threading.Lock()
        self.lcd = lcd
        self.line1 = "a"
        self.line2 = "b"

    def swap(self,line1,line2):
        self.line1 = line1
        self.line2 = line2

    def exit(self):
        thread.exit()

    def run(self):
        while True:
            self.lcd.update(self.line1+"\n"+self.line2)
            time.sleep(1.0)



class LCDHardware(object):
    def __init__(self):
        import Adafruit_CharLCD as LCD
        self.lcd = LCD.Adafruit_CharLCDPlate()
        self.lcd.clear()
        self.lcd.message('initialized')
        self.q=False

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

    def update(self,string):
        self.lcd.clear()
        self.lcd.set_color(self.color[0],self.color[1],self.color[2])
        self.lcd.message(str(string))
    
    def isButtonPressed(self):
        for button in self.buttons:
            if self.lcd.is_pressed(button[0]):
                return button[1]
            else
                return False





class LCDDisplay(Observer):
    '''observer that updates the display when it is notified by the subject'''

    def __init__(self,LCDHardware,subject):
        super(LCDDisplay,self).__init__(subject)


    def notify(self,observable, *args, **kwargs):
        LCDHardware.update("got %s " % args)




class LCDButtonListener(threading.Thread):
    '''thread that listens to the lcd hardware to see if a button was pressed. can be used as observable'''
    def __init__(self,threadID,name,anLCD):
        self.LCD = anLCD
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

        def run(self):
            self.LCD.isButtonPressed()
            selflcd.is_pressed(button[0]):

    # def update(self,string):
    #     # make sure all these lcd commands get executed without interrupting
    #     self.threadLock.acquire()
    #     #self.lcd.clear()
    #     self.lcd.set_color(self.color[0],self.color[1],self.color[2])
    #     self.lcd.message(str(string))
    #     self.threadLock.release()



    # Show button state.
    def run(self):
        print "starting " + self.name
        while True:
        # Loop through each button and check if it is pressed.
            
            if self.LCD.isButtonPressed:
                print self.LCD.isButtonPressed

            # for button in self.buttons:
            #     if self.lcd.is_pressed(button[0]):
            #         # Button is pressed, change the message and backlight.
            #         #self.lcd.clear()
            #         #self.lcd.message(button[1])
            #         #self.lcd.set_color(button[2][0], button[2][1], button[2][2])
            #         self.color=[button[2][0], button[2][1], button[2][2]]
            #         self.update(button[1])
            #         # print button[0]
            #         if button[0]==0:
            #             # select is pressed
            #             print "select pressed"
            #             return

            #             #thread.exit()
            #             # throws exeption








if __name__=='__main__':
    lcd1 = LCDHardware()
    
    lcdlistener1 = LCDButtonListener(1,'testlistenerthread',lcd1)
    lcdlistener1.start()    



    # lcd1.start()
    # lcd1.update("test\ntest")

    # anLCDDisplayUpdater = LCDDisplayUpdater(lcd1)
    # anLCDDisplayUpdater.start()

