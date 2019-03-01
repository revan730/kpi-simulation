import sys
import random
import numpy as np
from element import Element

class Process(Element):
    def __init__(self, delay, delay_std, maxParallel):
        super().__init__(delay, delay_std)
        self.queue = []
        self.state = []
        self.delay_std = delay_std
        self.maxParallel = maxParallel
        self.failure = 0
        self.maxQueue = 12345678999999
        self.meanQueue = 0.0
        self.workload = 0.0
        self.nextElements = None
        self.prob = None
        self.chambers = None
        self.lab = None
        self.registration = None

    def inAct(self, patient):
        if len(self.state) < self.maxParallel:
            self.state.append(patient)
        elif len(self.queue) < self.maxQueue:
            self.queue.append(patient)
        else:
            self.failure += 1
        # TODO: Set delay depending on patient type
        if self.name == 'doctors':
            self.setTnext(self.getTcurr() + patient['delay'])
        else:
            self.setTnext(self.getTcurr() + self.getDelay())
        #self.setTnext(self.getTcurr() + self.getDelay())

    
    def outAct(self):
        super().outAct()
        self.setTnext(sys.float_info.max)
        
        p = None
        if len(self.state) > 0:
            p = self.state.pop(0)
        
        self.setTnext(self.getTcurr() + self.getDelay())

        if len(self.getQueue()) > 0:
            pFromQueue = self.queue.pop(0)
            self.state.append(pFromQueue)
        if (self.nextElements) and p is not None:
            if self.name == 'doctors':
                if p['type'] == 1:
                    e = self.chambers
                else:
                    e = random.choice(self.nextElements)
            elif self.name == 'labs':
                if p['type'] == 2:
                    e = self.nextElements[0]
                else:
                    return
            else:
                e = random.choice(self.nextElements)
            e.inAct(p)

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
        self.meanQueue = self.getMeanQueue() + len(self.queue) * delta
        self.workload += len(self.state) * delta

    def getMeanQueue(self):
        return self.meanQueue

