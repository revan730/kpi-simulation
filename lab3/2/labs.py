import sys
import random
import numpy as np
from process import Process

class Labs(Process):
    def __init__(self, delay, st_dev=0, max_simult=1):
        super().__init__(delay, st_dev, max_simult)

    def outAct(self):
        super().outAct()
        self.setTnext(sys.float_info.max)
        
        p_type = None
        if len(self.state) > 0:
            p_type = self.state.pop(0)                
            
        if len(self.queue) > 0:
            p_type_queue = self.queue.pop(0)
            self.state.append(p_type_queue)
        if (p_type is not None):
            if p_type == 2:
                e = self.nextElements[0]
                e.inAct(p_type) 