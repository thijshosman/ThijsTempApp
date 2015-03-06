import threading
import time
import math
from observer import *
from lcdHardware import *



class LCDDisplayUpdater(threading.Thread):
    #deprecated
    '''periodically update the display'''
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


class LogObserver(Observer):
    '''log notifications to standard out'''
    def __init__(self,subject):
        super(LogObserver,self).__init__(subject)
    def notify(self,observable,*args,**kwargs):
        for name,value in kwargs.items():
            print '{0} = {1} from {2}'.format(name,value,observable)
        for arg in args:
            print '{0} from {1}'.format(arg,observable)


class LCDDisplay(Observer):
    '''observer that updates the display when it is notified by the subject'''

    def __init__(self,subject,LCDHardware):
        super(LCDDisplay,self).__init__(subject)
        self.LCDHardware = LCDHardware
        print "initialized display"

    def notify(self,observable, *args, **kwargs):
        # notify the screen
        kwargs['line1']=kwargs['button']
        if kwargs['button']=='Select':
            kwargs['color']=[1,0,0]
        else:
            kwargs['color']=[1,1,1]
        self.LCDHardware.update(*args, **kwargs)


#class buttonHandler(Observer):
#    '''buttonhandler'''
#    def __init__(self,subjectlistener):
#        super(buttonHandler,self).__init__(subjectlistener)
#
#    def notify(self,observable, *args, **kwargs):
#        if 'button' in kwargs.items():
#            print 'button pressed: {0}'.format(kwargs['button'])



class LCDButtonListener(threading.Thread):
    '''thread that listens to the lcd hardware to see if a button was pressed. can be used as observable'''
    def __init__(self,threadID,name,anLCD):
        self.LCD = anLCD
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.stop_event = threading.Event()
        self.observable=Observable(name)

    def broadcast(self,*args,**kwargs):
        self.observable.notify_observers(*args,**kwargs)

    def stop(self):
        self.stop_event.set()

    def run(self):
        while self.stop_event.is_set() == False:
            a=self.LCD.isButtonPressed()

            if a:
                self.broadcast(button=a)




            # directly notify lcdDisplay
            #if a:
            #    self.broadcast(a)
            #if a == 'Select':
            #    self.broadcast('hello',color=[1.0,0.0,0.0])



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

