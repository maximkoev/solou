import numpy as np



class OdeArgs:

    def __init__(self):
        self.__s1 = None
        self.__s2 = None
        self.__k1 = None
        self.__k2 = None
        self.__alp1 = None
        self.__alp2 = None
        self.__gam1 = None
        self.__gam2 = None
        self.__t0 = None
        self.__tn = None
        self.__At = None
        self.timeline = None

    def set_s1(self, s1):
        print('S1 is set to: ' + str(s1))
        self.__s1 = s1

    def get_timeline(self):
        if self.get_t0() == self.get_tn():
            self.timeline = np.linspace(0, self.get_tn(), 2, True)
        else:
            self.timeline = np.linspace(self.get_t0(), self.get_tn(), 45, True)
        return self.timeline

    def get_s1(self):
        if self.__s1 is None:
            ValueError('S1 is not initialized')
        return self.__s1

    def set_s2(self, s2):
        print('S2 is set to: ' + str(s2))
        self.__s2 = s2

    def get_s2(self):
        return self.__s2

    def set_k1(self, k1):
        print('k1 is set to: ' + str(k1))
        self.__k1 = k1

    def get_k1(self):
        return self.__k1

    def set_k2(self, k2):
        print('k2 is set to: ' + str(k2))
        self.__k2 = k2

    def get_k2(self):
        return self.__k2

    def get_alp1(self):
        return self.__alp1

    def set_alp1(self, alp1):
        print('alp1 is set to: ' + str(alp1))
        self.__alp1 = alp1

    def get_alp2(self):
        return self.__alp2

    def set_alp2(self, alp2):
        print('alp2 is set to: ' + str(alp2))
        self.__alp2 = alp2

    def get_gam1(self):
        return self.__gam1

    def set_gam1(self, gam1):
        print('gam1 is set to: ' + str(gam1))
        self.__gam1 = gam1

    def get_gam2(self):
        return self.__gam2

    def set_gam2(self, gam2):
        print('gam2 is set to: ' + str(gam2))
        self.__gam2 = gam2

    def get_t0(self):
        return self.__t0

    def set_t0(self, t0):
        print('t0 is set to: ' + str(t0))
        self.__t0 = t0

    def get_tn(self):
        return self.__tn

    def set_tn(self, tn):
        print('tn is set to: ' + str(tn))
        self.__tn = tn

    def set_at(self, at):
        self.__At = at

    def get_at(self, x, y):
        if self.__At is None:
            raise ValueError('A(t) method is not defined')
        at_dictionary = {
            'A1(t)': self.get_k1() / (self.get_k1() + self.get_k2()),
            'A2(t)': x / (x + y),
            'A3(t)': self.get_k1() ** self.get_alp1() / (
                    self.get_k1() ** self.get_alp1() + self.get_k2() ** self.get_alp2()),
            'A4(t)': x ** self.get_alp1() / (x ** self.get_alp1() + y ** self.get_alp2()),
            'A5(t)': self.get_alp1() / (self.get_alp1() + self.get_alp2())
        }
        print('at = ' + str(at_dictionary[self.__At]))
        return at_dictionary[self.__At]

    def get_at_keys(self):
        return ['A1(t)', 'A2(t)', 'A3(t)', 'A4(t)', 'A5(t)']