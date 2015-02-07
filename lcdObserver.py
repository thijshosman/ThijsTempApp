
import threading
import time
import math
from observer import *
from LCDHardware import *

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




class LCDDisplay(Observer):
    '''observer that updates the display when it is notified by the subject'''

    def __init__(self,subject,LCDHardware):
        super(LCDDisplay,self).__init__(subject)
        self.LCDHardware = LCDHardware
        print "initialized"

    def notify(self,observable, *args, **kwargs):
        self.LCDHardware.update(*args, **kwargs)





class LCDButtonListener(threading.Thread):
    '''thread that listens to the lcd hardware to see if a button was pressed. can be used as observable'''
    def __init__(self,threadID,name,anLCD):
        self.LCD = anLCD
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.LCDButtonObservable=Observable()

    def broadcast(self,buttonPressed):
        self.LCDButtonObservable.notify_observers('but: %s' % buttonPressed)

    def run(self):
        while True:
            a=self.LCD.isButtonPressed()
            if a:
                self.broadcast(a)
                #print "button pressed: %s" % selflcd.is_pressed(button[0])
                #print "button pressed: "

    # def update(self,string):
    #     # make sure all these lcd commands get executed without interrupting
    #     self.threadLock.acquire()
    #     #self.lcd.clear()
    #     self.lcd.set_color(self.color[0],self.color[1],self.color[2])
    #     self.lcd.message(str(string))
    #     self.threadLock.release()



    # Show button state.
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

    # init hardware
    lcd1 = LCDHardware()

    #while True:
    #    lcd1.isButtonPressed()


    # create listener/observable for buttons that listens to lcd1
    lcdlistener1 = LCDButtonListener(1,'testlistenerthread',lcd1)

    # create display observer and let it listen to the lcdlistener observable
    display1 = LCDDisplay(lcdlistener1.LCDButtonObservable,lcd1)

    # see if observer works
    # lcdlistener1.broadcast('testbutton')

    # start listening for buttons
    lcdlistener1.start()

    do_exit = False
    while do_exit == False:
        try:
            # sleep some time
            time.sleep(0.1)
        except KeyboardInterrupt:
            # Ctrl+C was hit - exit program
            do_exit = True

    # stop all running threads
    lcdlistener1.stop()


    # lcd1.start()
    # lcd1.update("test\ntest")

    # anLCDDisplayUpdater = LCDDisplayUpdater(lcd1)
    # anLCDDisplayUpdater.start()

