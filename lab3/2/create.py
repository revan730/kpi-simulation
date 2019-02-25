from element import Element

class Create(Element):
    def __init__(self, delay):
        super().__init__(delay)

    def outAct(self):
        super().outAct(1)
        self.setTnext(self.getTcurr() + self.getDelay())
        self.getNextElement().inAct(1)
