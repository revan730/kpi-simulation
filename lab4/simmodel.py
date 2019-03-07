from create import Create
from process import Process
from model import Model
import random

class SimModel:
    delays = [0.2, 0.4, 0.9, 0.15]
    def createElements(self, count):
        c = Create(2)
        c.name = 'CREATOR'
        elementsList = [c]
        for i in range(1, count):
            e = Process(random.choice(self.delays), 1)
            e.maxQueue = 124325435
            e.name = 'PROCESSOR {}'.format(i)
            #print(i)
            #print(elementsList[i - 1].name)
            elementsList[i - 1].setNextElement(e)
            elementsList.append(e)
        
        return elementsList

    def main(self, count):

        elementsList = self.createElements(count)
        #print(elementsList)
        model = Model(elementsList)    
        return model.simulate(1000)

    
