from model.OdeArgs import OdeArgs


class Tab:
    def __init__(self, args: OdeArgs, ui):
        self.args = args
        self.ui = ui


    def onS1Change(self, text):
        self.onChange(text, self.args.set_s1)
    def onS2Change(self, text):
        self.onChange(text, self.args.set_s2)
    def onK1Change(self, text):
        self.onChange(text, self.args.set_k1)
    def onK2Change(self, text):
        self.onChange(text, self.args.set_k2)
    def onT0Change(self, text):
        self.onChange(text, self.args.set_t0)
    def onTnChange(self, text):
        self.onChange(text, self.args.set_tn)
    def onAlp1Change(self, text):
        self.onChange(text, self.args.set_alp1)

    def onAlp2Change(self, text):
        self.onChange(text, self.args.set_alp2)

    def onGam1Change(self, text):
        self.onChange(text, self.args.set_gam1)

    def onGam2Change(self, text):
        self.onChange(text, self.args.set_gam2)


    def onChange(self, text, func):
        try:
            func(float(text))
            self.checkOnEdit()
        except BaseException as e:
            print('Error on value parsing: ',e)

    def checkOnEdit(self):
        args = [self.args.get_tn(), self.args.get_t0(), self.args.get_s1(), self.args.get_s2(), self.args.get_k1(),
                self.args.get_k2(), self.args.get_alp2(), self.args.get_alp1(), self.args.get_gam1(),
                self.args.get_gam2()]
        _i = 0
        for arg in args:
            if arg is not None:
                _i = _i + 1

        if _i == 10:
            print('trace')
            print(self.__class__.__name__)
            print('==============================')
            if self.__class__.__name__ == "MapTab":
                self.ui.calc_mapper.setEnabled(True)
            else:
                self.ui.pushButton.setEnabled(True)



