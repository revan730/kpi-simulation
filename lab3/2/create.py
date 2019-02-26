from element import Element

class Create(Element):
    def __init__(self, delay):
        super().__init__(delay)

    def outAct(self):
        super().outAct()
        self.setTnext(self.getTcurr() + self.getDelay())
        #TODO: Generate 3 types of patients
        self.getNextElement().inAct({ type: 1 })
