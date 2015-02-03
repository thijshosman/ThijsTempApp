from observer import *

class observer1(Observer):
    def notify(self,observable, *args, **kwargs):
        print "observer1 is told %s from %s" % (args,observable)

class observer2(Observer):
    def notify(self,observable, *args, **kwargs):
        print "observer2 is different and is told %s from %s" % (args,observable)


class subject1(Observable):
	#def __init__(self):
	#	Observable.__init__()

	def broadcast(self):
		self.notify_observers('broadcast from subject1 object')


subject = subject1()
firstObserver = observer1(subject)
secondObserver = observer2(subject)
subject.broadcast()
#subject.notify_observers('test')