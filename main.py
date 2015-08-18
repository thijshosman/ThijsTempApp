import time
import lib.observer as observer
import lib.temp as temp
import lib.plotlyObserver as plotly
import lib.lcdObserver as lcdO
import lib.lcdHardware as lcdH

class mainLoop(observer.MultiObserver):
    '''main event loop'''
    def __init__(self):
        super(mainLoop,self).__init__()

        # init hardware class for lcd display and temp sensor
        self.lcd1 = lcdH.LCDHardware()
        self.aSensor = temp.tempSensor()

        # create a poller for the temp sensor
        self.aTempPoller = temp.sensorPoller(self.aSensor,interval=60)

        # log temperatures to plotly by adding plotlyobserver
        self.plotlyobstemp = plotly.plotlyObserver(self.aTempPoller.observable,'config.json','test stream plot')

        # add the temppoller observable to the list to be observed
        self.add_observable(self.aTempPoller.observable)

        # init listener thread and start listening to button presses on lcd1
        self.lcdlistener1 = lcdO.LCDButtonListener(1,'button',self.lcd1)

        # add the lcdlistener to the list to be observed
        self.add_observable(self.lcdlistener1.observable)



        # start the buttonlisten thread
        self.lcdlistener1.start()
        self.aTempPoller.start()

    def notify(self,observable, *args, **kwargs):
        # gets called by observables registered in constructor (atemppoller and buttonlistener)
        print('Got', args, kwargs, 'From', observable.name)

        # temp updated
        if observable.name == 'temp':
            self.lcd1.update(line1='temp=%.1fC/%.0fF' % (kwargs['value'],kwargs['value']*9.0/5.0+32))
            t = kwargs['timestamp']
            self.lcd1.update(line2='%02d:%02d' % (time.localtime(t).tm_hour,time.localtime(t).tm_min) )
        elif observable.name == 'button':
            buttonName = kwargs['button']
            if buttonName == 'Right':
                newcolor = self.lcd1.nextColor()
                self.lcd1.update(line2=newcolor)
            elif buttonName == 'Left':
                newcolor = self.lcd1.previousColor()
                self.lcd1.update(line2=newcolor)


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



