from element import Element
import numpy as np

delays = {
    1: 1.5,
    2: 4.0,
    3: 3.0
}


class Create(Element):
    def __init__(self, delay):
        super().__init__(delay)

    def outAct(self):
        super().outAct()
        self.setTnext(self.getTcurr() + self.getDelay())
        #TODO: Generate 3 types of patients
        patientType = np.random.choice([1, 2, 3], p=[0.5, 0.1, 0.4])
        self.getNextElement().inAct({ "type": patientType, "delay": delays[patientType]})
