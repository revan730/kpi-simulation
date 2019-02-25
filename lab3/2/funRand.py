import random
import math
import numpy as np

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

    @staticmethod
    def erlang(k, theta):
        return np.random.gamma(k, theta)
