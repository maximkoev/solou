import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from model.OdeArgs import OdeArgs


class OdeSolve:

    def __init__(self, args: OdeArgs):
        self.__s1 = args.get_s1()
        self.__s2 = args.get_s2()
        self.__k1 = args.get_k1()
        self.__k2 = args.get_k2()
        self.__alp1 = args.get_alp1()
        self.__alp2 = args.get_alp2()
        self.__gam1 = args.get_gam1()
        self.__gam2 = args.get_gam2()
        self.__result = None
        self.__timeline = args.get_timeline()
        self.__At = lambda x, y: args.get_at(x, y)
        self.__delta = args.get_STP()

    def model45(self, z, t):
        print(f'Model initialized with z = {z}, t = {t}, stp = {self.stp(t)}')
        x = z[0]
        y = z[1]

        k1 = self.__At(x, y) * self.stp(t) * \
             ((self.__s1 * x ** self.__alp1 + self.__s2 * y ** self.__alp2) - self.__gam1 * x)
        k2 = (1 - self.__At(x, y)) * self.stp(t) * \
             ((self.__s1 * x ** self.__alp1 + self.__s2 * y ** self.__alp2) - self.__gam2 * y)
        return [k1, k2]

    def calc(self):
        z0 = [self.__k1, self.__k2]
        #print(f"timeline is: {self.__timeline}")
        self.__result = odeint(self.model45, z0, self.__timeline)
        print("===================result===================")
        print(self.__result)
        print("=============================================")
        return self.__result

    def getTimeline(self):
        return self.__timeline

    def buildPlot(self):
        plt.plot(self.__timeline, self.__result[:, 0], 'b-', label='K1')
        plt.plot(self.__timeline, self.__result[:, 1], 'r--', label='K2')
        plt.ylabel('response')
        plt.xlabel('time')
        plt.legend(loc='best')
        plt.show()

    # Calculate scientific and technical progress
    stp = lambda self, t: np.exp(t * self.__delta)
