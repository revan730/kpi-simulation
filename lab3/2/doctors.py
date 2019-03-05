import sys
import random
import numpy as np
from process import Process

class Doctor(Process):
    def __init__(self, delay, st_dev=0, max_simult=1):
        super().__init__(delay, st_dev, max_simult)
        self.to_lab_amount = 0

    def outAct(self):
        super().outAct()
        self.setTnext(sys.float_info.max)
        
        p_type = None
        if len(self.state) > 0:
            for i in range(len(self.state)):
                if self.state[i] == 1:
                    p_type = self.state.pop(i)
                    break
            if (p_type is None):
                p_type = self.state.pop(0)
            
        if len(self.queue) > 0:
            p_type_queue = self.queue.pop(0)
            self.state.append(p_type_queue)
        if (p_type is not None):
            if p_type == 1:
                e = self.nextElements[0]
            else:
                e = self.nextElements[1]

                self.to_lab_amount += 1
            e.inAct(p_type) 

    def doStatistics(self, delta, state):
        self.meanQueue = self.meanQueue + len(self.queue) * delta
        self.workload += (len(self.state)) * delta
        
        self.time_wait += (len(self.queue) + len(self.state)) * delta
        self.in_wait += (len(self.queue) + len(self.state))
        if (state is not None) and (state in [2, 3]):
            self.delay_sum += delta