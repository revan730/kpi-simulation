import sys
from process import Process
import pandas as pd
import numpy as np
import time

class Model:
    def __init__(self, elements):
        self.elementsList = elements
        self.tnext = 0
        self.event = 0
        self.tcurr = self.tnext

    def get(self, id):
        for e in self.elementsList:
            if e.getId() is id:
                return e

    def simulate(self, t):
        currentTime = time.time()
        while self.tcurr < t:
            self.tnext = sys.float_info.max
            name = ''
            for e in self.elementsList:
                if e.getTnext() < self.tnext:
                    self.tnext = e.getTnext()
                    self.event = e.getId()
                    name = e.getName()
            for e in self.elementsList:
                e.doStatistics(self.tnext - self.tcurr)
            self.tcurr = self.tnext
            for e in self.elementsList:
                e.setTcurr(self.tcurr)
            self.get(self.event).outAct()
            for e in self.elementsList:
                if e.getTnext() is self.tcurr:
                    e.outAct()
        #self.printResult()
        end = time.time()
        return {"time": end - currentTime, "tacts": self.tcurr}

    def printInfo(self):
        for e in self.elementsList:
            e.printInfo()

    def returnResult(self):
        res = pd.DataFrame()
        i = 0
        for e in self.elementsList:
            i += 1
            e.printResult()
            if isinstance(e, Process):
                mean = e.meanQueue / self.tcurr
                workload = e.workload / self.tcurr
                if i == 5:
                    workload -= 1
                   
                res = res.append(pd.DataFrame({
                    'name': [e.name],
                    'mean': [mean],
                    'workload': [workload]
                }))
        return res

    def printResult(self):
        print('\n____________________________')
        print('\nRESULTS')
 
        for e in self.elementsList:
            e.printResult()
            if isinstance(e, Process):
                mean = e.meanQueue / self.tcurr
                failure = e.failure / e.quantity
                wait = e.meanQueue / (e.quantity + e.failure)
                workload = e.workload / self.tcurr
                print('name {} delay_mean {} quantity {} mean queue {} failure {} wait {} workload {}'
                .format(e.name, round(e.delayMean, 4), e.quantity, round(mean, 4), round(failure, 4), round(wait, 4), round(workload, 4)))

