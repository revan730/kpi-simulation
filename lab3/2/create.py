from element import Element
import numpy as np

delays = {
    1: 1/15,
    2: 1/40,
    3: 1/30
}


class Create(Element):
    def __init__(self, delay):
        super().__init__(delay)

    def outAct(self):
        super().outAct()
        patient_type = np.random.choice([1, 2, 3], p=[0.5, 0.1, 0.4])
        
        self.setTnext(self.getTcurr() + self.getDelay())
        
        self.getNextElement().setDelayMean(delays[patient_type])
        self.getNextElement().inAct(patient_type)