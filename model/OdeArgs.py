class OdeArgs:

    def __init__(self):
        self.s1 = None
        self.s2 = None
        self.k1 = None
        self.k2 = None
        self.alp1 = None
        self.alp2 = None
        self.gam1 = None
        self.gam2 = None
        self.t0 = None
        self.tn = None
        self.__At = None

    def set_s1(self, s1):
        print('S1 is set to: ' + str(s1))
        self.s1 = s1

    def get_s1(self):
        print('get_s1 is called with value' + str(self.s1))
        if self.s1 is None:
            ValueError('S1 is not initialized')
        return self.s1

    def set_s2(self, s2):
        print('S2 is set to: ' + str(s2))
        self.s2 = s2

    def get_s2(self):
        return self.s2

    def set_k1(self, k1):
        print('k1 is set to: ' + str(k1))
        self.k1 = k1

    def get_k1(self):
        return self.k1

    def set_k2(self, k2):
        print('k2 is set to: ' + str(k2))
        self.k2 = k2

    def get_k2(self):
        return self.k2

    def get_alp1(self):
        return self.alp1

    def set_alp1(self, alp1):
        print('alp1 is set to: ' + str(alp1))
        self.alp1 = alp1

    def get_alp2(self):
        return self.alp2

    def set_alp2(self, alp2):
        print('alp2 is set to: ' + str(alp2))
        self.alp2 = alp2

    def get_gam1(self):
        return self.gam1

    def set_gam1(self, gam1):
        print('gam1 is set to: ' + str(gam1))
        self.gam1 = gam1

    def get_gam2(self):
        return self.gam2

    def set_gam2(self, gam2):
        print('gam2 is set to: ' + str(gam2))
        self.gam2 = gam2

    def get_t0(self):
        return self.t0

    def set_t0(self, t0):
        print('t0 is set to: ' + str(t0))
        self.t0 = t0

    def get_tn(self):
        return self.tn

    def set_tn(self, tn):
        print('tn is set to: ' + str(tn))
        self.tn = tn

    def set_at(self, at):
        self.__At = at

    def get_at(self, x, y):
        at_dictionary = {
            'A1(t)': self.get_k1() / (self.get_k1() + self.get_k2()),
            'A2(t)': x / (x + y),
            'A3(t)': self.get_k1() ** self.get_alp1() / (
                        self.get_k1() ** self.get_alp1() + self.get_k2() ** self.get_alp2()),
            'A4(t)': x ** self.get_alp1() / (x ** self.get_alp1() + y ** self.get_alp2()),
            'A5(t)': self.get_alp1() / (self.get_alp1() + self.get_alp2())
        }
        if self.__At is None:
            print('at returned is: A1(t)')
            return at_dictionary['A1(t)']
        else:
            print('at = '+str(at_dictionary[self.__At]))
            return at_dictionary[self.__At]
