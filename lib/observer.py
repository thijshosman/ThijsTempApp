import sys


class Observable(object):
    def __init__(self,name=''):
        self.__observers = []
        self.name=name

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            try:
                observer(self, *args, **kwargs)
            except:
                print "Unexpected error:", sys.exc_info()[0]

class Observer(object):
    def __init__(self, observable):
        observable.register_observer(self.notify)

    def notify(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)

class MultiObserver(object):
    '''single observer for multiple observables. notify method intended to be used for event handlers'''
    def __init__(self):
        self.observables = []

    def add_observable(self,observable):
        self.observables.append(observable)
        observable.register_observer(self.notify)

    def notify(self,observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)


if __name__ == '__main__':
    subject = Observable()

    observer = Observer(subject)
    subject.notify_observers('test')


    subject2 = Observable('testname')
    aMultiObserver = MultiObserver()
    aMultiObserver.add_observable(subject)
    aMultiObserver.add_observable(subject2)
    subject2.notify_observers('test from 2')
    subject.notify_observers('test from 1')
    print aMultiObserver.observables
    # test for git

