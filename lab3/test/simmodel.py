from create import Create
from process import Process
from model import Model

class SimModel:
    def main(self):
        c = Create(2)
        p1 = Process(.6, 1)
        p2 = Process(.3, 1)
        p3 = Process(.4, 1)
        p4 = Process(.1, 2)


        print('id0 = {} id1= {} '.format(c.getId(), p1.getId()))
        c.setNextElement(p1)
        c.setName('CREATOR')
        p1.setName('PROCESSOR1')
        p2.setName('PROCESSOR2')
        p3.setName('PROCESSOR3')
        p4.setName('PROCESSOR4')
        c.setDistribution('exp')
        p1.setDistribution('exp')
        p2.setDistribution('exp')
        p3.setDistribution('exp')
        p4.setDistribution('exp')

        p1.setNextElements([p2, p3, p4, None])
        p1.elementsProbabilities = [0.15, 0.13, 0.3, 0.42]

        p2.setNextElements([p1])
        p3.setNextElements([p1])
        p4.setNextElements([p1])


        elementsList = [c, p1, p2, p3, p4]
        model = Model(elementsList)    
        model.simulate(1000000.0)

        res = model.returnResult()
        res['theoretical_mean_queue'] = [1.786, 0.003, 0.004, 0.00001]
        res['theoretical_workload'] = [0.714, 0.054, 0.062, 0.036]
        res['queue_accuracy'] = 100*(abs(res.eval('mean - theoretical_mean_queue')) / res['theoretical_mean_queue'])
        res['workload_accuracy'] = 100*(abs(res.eval('workload - theoretical_workload')) / res['theoretical_workload'])
        print(res)
    
