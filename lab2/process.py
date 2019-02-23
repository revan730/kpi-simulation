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
        self.workload = 0.0
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
    
    def outAct(self):
        super().outAct(1)
        self.setTnext(sys.float_info.max)
        self.state -= 1
        if self.getQueue() > 0:
            self.queue -= 1
            self.state += 1
            self.setTnext(self.getTcurr() + self.getDelay())
        if (self.nextElements):
            e = random.choice(self.nextElements)
            e.inAct(1)

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
        self.workload += self.state * delta

    def getMeanQueue(self):
        return self.meanQueue

