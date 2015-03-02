
import threading
import time
import math
from observer import *
from lcdHardware import *
from temp import *

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
        self.observable=Observable()

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

class mainLoop(MultiObserver):
    '''main event loop'''
    def __init__(self):
        super(mainLoop,self).__init__()

        # init hardware class for lcd display and temp sensor
        self.lcd1 = LCDHardware()
        self.aSensor = tempSensor()

        # create a poller for the temp sensor
        self.aTempPoller = sensorPoller(self.aSensor,interval=2)

        # add the temppoller observable to the list to be observed
        self.add_observable(self.aTempPoller.observable)

        # init listener thread and start listening to button presses on lcd1
        self.lcdlistener1 = LCDButtonListener(1,'buttonpresslistenerthread',self.lcd1)

        # add the lcdlistener to the list to be observed
        self.add_observable(self.lcdlistener1.observable)

        # register the command line observer with the lcdlistener observable
        # ButtonLog = LogObserver(lcdlistener1.LCDButtonObservable)




        # start the buttonlisten thread
        self.lcdlistener1.start()
        self.aTempPoller.start()

    def notify(self,observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)


    def stop(self):
        # stop polling temp
        self.aTempPoller.stop()

        # stop listening for button input
        self.lcdlistener1.stop()




if __name__=='__main__':

    handler = mainLoop()

    do_exit = False
    while do_exit == False:
        try:
            # sleep some time
            time.sleep(0.1)
        except KeyboardInterrupt:
            # Ctrl+C was hit - exit program
            do_exit = True

    handler.stop()

    # ### LCD stuff

    # # init hardware
    # lcd1 = LCDHardware()

    # # create listener/observable for buttons that listens to lcd1
    # lcdlistener1 = LCDButtonListener(1,'testlistenerthread',lcd1)

    # # create display observer and let it listen to the lcdlistener observable
    # # display1 = LCDDisplay(lcdlistener1.LCDButtonObservable,lcd1)
    # log1 = LogObserver(lcdlistener1.LCDButtonObservable)

    # # start listening for buttons
    # lcdlistener1.start()
    # # lcdlistener1.broadcast(button='left')

    # ### Temp stuff
    # aSensor = tempSensor()

    # aTempPoller = sensorPoller(aSensor,interval=2)

    # # register default observer with the poller
    # # firstobserver = Observer(aTempPoller.observable)

    # # add the temppoller to the list of observabes display1 observes
    # # aTempPoller.registerExtraObserver(display1)
    # display1 = LCDDisplay(aTempPoller.observable,lcd1)

    # # start polling temperature
    # aTempPoller.start()



    # do_exit = False
    # while do_exit == False:
    #     try:
    #         # sleep some time
    #         time.sleep(0.1)
    #     except KeyboardInterrupt:
    #         # Ctrl+C was hit - exit program
    #         do_exit = True

    # # stop all running threads
    # lcdlistener1.stop()
    # aTempPoller.stop()



