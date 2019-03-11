from funRand import FunRand

class Element:
    nextId = 0

    def __init__(self, delay):
        if delay is not None:
            self.name = 'anonymous'
            self.tnext = 0
            self.delayMean = delay
            self.delayDev = 0
            self.quantity = 0
            self.distribution = 'exp'
            self.tcurr = self.tnext
            self.state = 0
            self.nextElement = None
            self.nextElements = []
            self.id = Element.nextId
            Element.nextId = Element.nextId + 1
            self.name = 'element'+str(self.id)
        else:
            self.tnext = 0
            self.delayMean = 1.0
            self.delayDev = 0
            self.quantity = 0
            self.distribution = 'exp'
            self.tcurr = self.tnext
            self.state = 0
            self.nextElement = None
            self.nextElements = []
            self.id = Element.nextId
            Element.nextId = Element.nextId + 1
            self.name = 'element'+str(self.id)

    def getDelayMin(self):
        return self.delayMean

    def getDelay(self):
        delay = self.getDelayMin()
        if self.getDistribution() == 'exp':
            delay = FunRand.exp(self.getDelayMean())
        elif self.getDistribution() == 'norm':
            delay = FunRand.norm(self.getDelayMean(), self.getDelayDev())
        elif self.getDistribution() == 'unif':
            delay = FunRand.unif(self.getDelayMin(), self.getDelayDev())
        elif self.getDistribution() == 'unif':
            delay = self.getDelayMean()
        return delay

    def getDelayDev(self):
        return self.delayDev

    def setDelayDev(self, delayDev):
        self.delayDev = delayDev

    def getDistribution(self):
        return self.distribution

    def setDistribution(self, dist):
        self.distribution = dist

    def getQuantity(self):
        return self.quantity

    def getTcurr(self):
        return self.tcurr

    def setTcurr(self, tcurr):
        self.tcurr = tcurr

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def getNextElement(self):
        return self.nextElement

    def setNextElement(self, element):
        self.nextElement = element

    def inAct(self):
        pass

    def outAct(self):
        self.quantity = self.quantity + 1

    def getTnext(self):
        return self.tnext

    def setTnext(self, tnext):
        self.tnext = tnext

    def getDelayMean(self):
        return self.delayMean

    def setDelayMean(self, mean):
        self.delayMean = mean

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def printResult(self):
        print('{} quantity = {} '.format(self.name, self.quantity))

    def printInfo(self):
        print('{} state = {} tnext = {} quantity = {} '.format(self.name, self.state, self.tnext, self.quantity))

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def doStatistics(self, delta):
        pass

