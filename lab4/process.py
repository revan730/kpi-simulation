import sys
import random
import numpy as np
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
        self.elementsProbabilities = None

    def inAct(self):
        if self.state < self.maxParallel:
            self.state = self.maxParallel
        elif self.queue < self.maxQueue:
            self.queue += 1
        else:
            self.failure += 1
        self.setTnext(self.getTcurr() + self.getDelay())
    
    def outAct(self):
        super().outAct()
        self.setTnext(sys.float_info.max)
        self.state -= 1
        if self.getQueue() > 0:
            self.queue -= 1
            self.state += 1
            self.setTnext(self.getTcurr() + self.getDelay())
        if self.nextElement:
            self.nextElement.inAct()

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
