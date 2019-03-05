import sys
from process import Process
import pandas as pd
import numpy as np

class Model:
    def __init__(self, elements):
        self.elementsList = elements
        self.tnext = 0.0
        self.event = 0
        self.tcurr = self.tnext

    def get(self, id):
        for e in self.elementsList:
            if e.getId() is id:
                return e

    def simulate(self, time):
        while self.tcurr < time:
            self.tnext = sys.float_info.max
            name = ''
            for e in self.elementsList:
                if e.getTnext() < self.tnext:
                    self.tnext = e.getTnext()
                    self.event = e.getId()
                    name = e.getName()
            #print("It's time for event in {} , time = {}".format(name ,self.tnext))
            for e in self.elementsList:
                e.doStatistics(self.tnext - self.tcurr)
            self.tcurr = self.tnext
            for e in self.elementsList:
                e.setTcurr(self.tcurr)
            self.get(self.event).outAct()
            for e in self.elementsList:
                if e.getTnext() is self.tcurr:
                    e.outAct()
            #self.printInfo()
        self.printResult()
        #print(self.get_results())
        #self.get_results()

    def printInfo(self):
        for e in self.elementsList:
            e.printInfo()

    def get_results(self):
        res = []
        for e in self.elementsList:
            if isinstance(e, Process):
                mean = e.meanQueue / self.tcurr
                failure = e.failure / e.quantity
                wait = e.meanQueue / (e.quantity + e.failure)
                workload = e.workload / self.tcurr
                print('name {} max_queue {} max_parallel {} delay_mean {} quantity {} dist {} mean queue {} failure {} wait {} workload {}'
                .format(e.name, e.maxQueue, e.maxParallel, e.delayMean, e.quantity, e.distribution, mean, failure, wait, workload))
                '''res.append({
                    'name': e.name,
                    'max_queue': e.maxQueue,
                    'max_parallel': e.maxParallel,
                    'delay_mean': e.delayMean,
                    #'delay_std': e.get_delay_std(),
                    'quantity': e.quantity,
                    'distribution': e.distribution,
                    'mean queue size': mean,
                    'failure probability': failure,
                    'avg wait time': wait,
                    'workload': workload     
                })'''
        
        #return res

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
 
        i = 0
        for e in self.elementsList:
            i += 1
            e.printResult()
            if isinstance(e, Process):
                mean = e.meanQueue / self.tcurr
                failure = e.failure / e.quantity
                wait = e.meanQueue / (e.quantity + e.failure)
                workload = e.workload / self.tcurr
                if i == 5:
                    workload -= 1
                print('name {} delay_mean {} quantity {} mean queue {} failure {} wait {} workload {}'
                .format(e.name, round(e.delayMean, 4), e.quantity, round(mean, 4), round(failure, 4), round(wait, 4), round(workload, 4)))

