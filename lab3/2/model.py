import sys
from process import Process
from doctors import Doctor
from create import Create

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
                if isinstance(e, Doctor):
                    if len(e.state) > 0:    
                        e.doStatistics(self.tnext - self.tcurr, e.state[0])
                    else:
                        e.doStatistics(self.tnext - self.tcurr, None)
                else:
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

    def printResult(self):
        print('\n____________________________')
        print('\nRESULTS')
        
        t_w = 0
        patients = 0
       
        for e in self.elementsList:
            if isinstance(e, Create):
                patients = e.quantity
            e.printResult()
            if isinstance(e, Process):
                
                t_w += e.time_wait
                #patients += e.in_wait
                
                mean = e.meanQueue / self.tcurr

                workload = e.workload / self.tcurr
                print('name {} max_parallel {}  quantity {} mean queue {} workload {}'
                .format(e.name, e.maxParallel, e.quantity, round(mean, 3), round(workload, 3)))
                if isinstance(e, Doctor):
                    time_between_lab = e.delay_sum / e.to_lab_amount
                    print('Avg trip from doctor to lab duration is ', round(time_between_lab, 3))
                
        avg_time = t_w / patients
        print('Average time in the hospital is ', round(avg_time, 3))