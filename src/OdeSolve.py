import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from model import OdeArgs


# function that returns dz/dt


class OdeSolve():

    def __init__(self, args: OdeArgs.OdeArgs):
        self.__s1 = args.get_s1()
        self.__s2 = args.get_s2()
        self.__k1 = args.get_k1()
        self.__k2 = args.get_k2()
        self.__alp1 = args.get_alp1()
        self.__alp2 = args.get_alp2()
        self.__gam1 = args.get_gam1()
        self.__gam2 = args.get_gam2()
        self.__result = None
        self.__timeline = np.linspace(args.get_t0(), args.get_tn(), 4, True)
        self.__At = lambda x,y: args.get_at(x,y)

    def model(self, z, t):
        print('model is initialized')
        x = z[0]
        y = z[1]

        print('mode s1 = ' + str(self.__s1))
        dxdt = self.__At(x, y) * ((self.__s1 * x ** self.__alp1 + self.__s2 * y ** self.__alp2) - self.__gam1 * x)
        dydt = (1 - self.__At(x, y)) * ((self.__s1 * x ** self.__alp1 + self.__s2 * y ** self.__alp2) - self.__gam2 * y)
        return [dxdt, dydt]

    def calc(self):
        print('calc method is initialized')
        # initial condition
        z0 = [self.__k1, self.__k2]
        _AT = self.__At(self.__k1, self.__k2)
        self.__result = odeint(self.model, z0, self.__timeline)
        print(self.__result)
        return self.__result

    def getTimeline(self):
        return self.__timeline

    def buildPlot(self):
        plt.plot(self.__timeline, self.__result[:, 0], 'b-', label=r'$\frac{dx}{dt}=3 \; \exp(-t)$')
        plt.plot(self.__timeline, self.__result[:, 1], 'r--', label=r'$\frac{dy}{dt}=-y+3$')
        plt.ylabel('response')
        plt.xlabel('time')
        plt.legend(loc='best')
        plt.show()
