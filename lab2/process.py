import sys
import random
from element import Element

class Process(Element):
    def __init__(self, delay, maxParallel):
        super().__init__(delay)
        self.queue = 0
        self.maxParallel = maxParallel
        self.failure = 0
        self.maxQueue = 12345678999999
        self.meanQueue = 0.0
        self.nextElements = None

    def inAct(self, i):
        delta = self.maxParallel - self.state
        if i < delta:
            self.state += i
            i = 0
        else:
            i -= delta
            self.state = self.maxParallel
        self.setTnext(self.getTcurr() + self.getDelay())
        if i > 0:
            delta = self.maxQueue - self.queue
            if i < delta:
                self.queue += i
                i = 0
            else:
                i -= delta
                self.queue = self.maxQueue
        if i > 0:
            self.failure += i

        '''if self.getState() < self.maxParallel:
            self.setState(self.getState() + 1)
            self.setTnext(self.getTcurr() + self.getDelay())
        else:
            if self.getQueue() < self.getMaxqueue():
                self.setQueue(self.getQueue() + 1)
            else:
                self.failure = self.failure + 1'''
    
    def outAct(self):
        outcoming = self.state
        super().outAct(self.state)
        self.setTnext(sys.float_info.max)
        self.setState(0)
        if self.getQueue() > 0:
            delta = self.maxParallel
            if self.queue < delta:
                self.state = self.queue
                self.queue = 0
            else:
                self.queue -= delta
                self.state = self.maxParallel
            self.setTnext(self.getTcurr() + self.getDelay())
        if (self.nextElements):
            e = random.choice(self.nextElements)
            e.inAct(outcoming)
            #for e in self.nextElements:
                #e.inAct(outcoming)

    def setNextElements(self, nextElements):
        self.nextElements = nextElements
    
    def getFailure(self):
        return self.failure

    def getQueue(self):
        return self.queue

    def setQueue(self, queue):
        self.queue = queue

    def getMaxqueue(self):
        return self.maxQueue
    
    def setMaxqueue(self, max):
        self.maxQueue = max

    def printInfo(self):
        super().printInfo()
        print('failure = {}'.format(self.getFailure()))

    def doStatistics(self, delta):
        self.meanQueue = self.getMeanQueue() + self.queue * delta

    def getMeanQueue(self):
        return self.meanQueue

