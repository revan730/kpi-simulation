import random
import math

class FunRand:
    @staticmethod
    def exp(timeMean):
        a = 0.0
        while a == 0.0:
            a = random.uniform(0, 1)
        a = -timeMean * math.log(a)
        return a
    
    @staticmethod
    def unif(timeMin, timeMax):
        a = 0.0
        while a == 0.0:
            a = random.uniform(0, 1)
        a = timeMin + a * (timeMax - timeMin)
        return a

    @staticmethod
    def norm(timeMean, timeDeviation):
        return random.gauss(timeMean, timeDeviation)
