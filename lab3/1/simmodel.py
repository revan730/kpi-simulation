from create import Create
from process import Process
from model import Model

class SimModel:
    def main(self):
        p11 = Process(1, 0.3, 1)
        p12 = Process(1, 0.3, 1)
        p11.otherProcess = p12
        p12.otherProcess = p11
        c = Create(.5)
        c.setNextElements([p11, p12])
        p11.setMaxqueue(3)
        p12.setMaxqueue(3)
        p11.state = 1
        p12.state = 1
        c.tnext = 0.1
        p11.queue = 2
        p12.queue = 2
        c.setName('CREATOR')
        p11.setName('PROCESSOR21')
        p12.setName('PROCESSOR22')
        c.setDistribution('exp')
        p11.setDistribution('exp')
        p12.setDistribution('exp')


        elementsList = [c,p11, p12]
        model = Model(elementsList)    
        model.simulate(1000.0)
    
