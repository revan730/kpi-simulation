from element import Element

class Create(Element):
    def __init__(self, delay):
        self.nextElements = []
        super().__init__(delay)

    def setNextElements(self, elems):
        self.nextElements = elems

    def outAct(self):
        super().outAct(1)
        self.setTnext(self.getTcurr() + self.getDelay())
        self.getNextElement().inAct(1)

    def getNextElement(self):
        queue_arr = [el.queue for el in self.nextElements]
        if (sum(queue_arr) == 0) or (queue_arr[1:] == queue_arr[:-1]):
            return self.nextElements[0]
        else:
            return self.nextElements[queue_arr.index(min(queue_arr))]
