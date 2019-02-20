import sys
from process import Process

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
            print("It's time for event in {} , time = {}".format(name ,self.tnext))
            for e in self.elementsList:
                e.doStatistics(self.tnext - self.tcurr)
            self.tcurr = self.tnext
            for e in self.elementsList:
                e.setTcurr(self.tcurr)
            self.get(self.event).outAct()
            for e in self.elementsList:
                if e.getTnext() is self.tcurr:
                    e.outAct()
            self.printInfo()
        self.printResult()

    def printInfo(self):
        for e in self.elementsList:
            e.printInfo()

    def printResult(self):
        print('\n-----------RESULTS----------')
        for e in self.elementsList:
            e.printResult()
            if isinstance(e, Process):
                mean = e.getMeanQueue()
                failure = e.getFailure() / e.getQuantity()
                print('mean length of queue = {} \n failure probability = {}'.format(mean, failure))
