from create import Create
from process import Process
from model import Model
from doctors import Doctor
from labs import Labs

class SimModel:
    def main(self):
        c = Create(1./15)
        c.setDistribution('exp')
        c.setName('creator')
        
        p0 = Doctor(0, 0, 2)
        p0.setName('doctors')
        p0.setDistribution('exp')
        
        p1 = Process(3, 8, 3)
        p1.setName('chambers')
        #p1.setDistribution('unif')
        p1.setDistribution('exp')
        
        p2 = Process(3, 4.5, 1)
        p2.setName('registration')
        #p2.set_distribution('erlang')
        p2.setDistribution('exp')
        #p2.maxQueue = 2

        p3 = Labs(2, 4, 2)
        p3.setName('lab')
        p3.setDistribution('exp')
        #p3.set_distribution('erlang')
        

        #p0.chambers = p1
        #p0.registration = p2
        c.nextElement = p0
        p0.setNextElements([p1, p2])
        p2.setNextElements([p3])
        p3.setNextElements([p0])

        elementsList = [c, p0, p1, p2, p3]
        model = Model(elementsList)    
        model.simulate(10000.0)
    
