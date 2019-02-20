from create import Create
from process import Process
from model import Model

class SimModel:
    def main(self):
        c = Create(2.0)
        p1 = Process(1.0, 2)
        p21 = Process(1.1, 1)
        p22 = Process(1.0, 2)
        p3 = Process(1.2, 1)
        print('id0 = {} id1= {} '.format(c.getId(), p1.getId()))
        c.setNextElement(p1)
        p1.setMaxqueue(5)
        p21.setMaxqueue(3)
        p22.setMaxqueue(2)
        p3.setMaxqueue(2)
        c.setName('CREATOR')
        p1.setName('PROCESSOR1')
        p21.setName('PROCESSOR21')
        p22.setName('PROCESSOR22')
        p3.setName('PROCESSOR3')
        c.setDistribution('exp')
        p1.setDistribution('exp')
        p21.setDistribution('exp')
        p22.setDistribution('exp')
        p3.setDistribution('exp')

        p1.setNextElements([p21, p22])
        p21.setNextElements([p3])
        p22.setNextElements([p3])


        elementsList = [c, p1, p21, p22, p3]
        model = Model(elementsList)    
        model.simulate(1000.0)
    
