import sys
import random
import numpy as np
from element import Element

class Process(Element):
    def __init__(self, delay, delay_std=0, maxParallel=1):
        super().__init__(delay, delay_std)
        self.queue = []
        self.state = []
        self.delay_std = delay_std
        self.maxParallel = maxParallel
        self.failure = 0
        self.maxQueue = 12345678999999
        self.meanQueue = 0.0
        self.workload = 0.0
        self.in_wait = 0
        self.time_wait = 0
        self.delay_sum = 0
        self.nextElements = None

    def inAct(self, p_type):
        if len(self.state) < self.maxParallel:
            self.state.append(p_type)
        elif len(self.queue) < self.maxQueue:
            self.queue.append(p_type)
        self.setTnext(self.getTcurr() + self.getDelay())

    
    def outAct(self):
        super().outAct()
        self.setTnext(sys.float_info.max)
        
        p_type = None
        if len(self.state) > 0:
            p_type = self.state.pop(0)
        
        if len(self.queue) > 0:
            p_type_queue = self.queue.pop(0)
            self.state.append(p_type_queue)
        
        if (self.nextElements) and (p_type is not None):
            e = random.choice(self.nextElements)
            e.inAct(p_type)
    

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
        self.meanQueue = self.meanQueue + len(self.queue) * delta
        self.workload += len(self.state) * delta
        
        self.time_wait += (len(self.queue) + len(self.state)) * delta
        self.in_wait += (len(self.queue) + len(self.state))
        self.delay_sum += delta

    def getMeanQueue(self):
        return self.meanQueue

