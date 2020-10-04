import numpy as np
from scipy.integrate import odeint
from model import OdeArgs


# function that returns dz/dt



class OdeSolve():

    def __init__(self, args: OdeArgs.OdeArgs):
        self.s1 = args.get_s1()
        self.s2 = args.get_s2()
        self.k1 = args.get_k1()
        self.k2 = args.get_k2()
        self.alp1 = args.get_alp1()
        self.alp2 = args.get_alp2()
        self.gam1 = args.get_gam1()
        self.gam2 = args.get_gam2()
        self.t0 = args.get_t0()
        self.tn = args.get_tn()

    def model(self, z, t):
        print('model is initialized')
        x = z[0]
        y = z[1]
        print('mode s1 = '+str(self.s1))
        dxdt = (x / (x + y)) * ((self.s1 * x ** self.alp1 + self.s2 * y ** self.alp2) - self.gam1 * x)
        dydt = (1 - (x / (x + y))) * ((self.s1 * x ** self.alp1 + self.s2 * y ** self.alp2) - self.gam2 * y)
        return [dxdt, dydt]


    def calc(self):
        print('calc method is initialized')
        # initial condition
        z0 = [self.k1, self.k2]
        # time points
        t = np.linspace(self.t0, self.tn, 4, True)
        print('=======================================')
        print(t)
        print('=======================================')
        # solve ODE
        z = odeint(self.model, z0, t)
        return z


# plot results
# plt.plot(t,z[:,0],'b-',label=r'$\frac{dx}{dt}=3 \; \exp(-t)$')
# plt.plot(t,z[:,1],'r--',label=r'$\frac{dy}{dt}=-y+3$')
# plt.ylabel('response')
# plt.xlabel('time')
# plt.legend(loc='best')
# plt.show()
