from PyQt5 import QtWidgets
from UI import mainView
from src import OdeSolve
from model import OdeArgs


class App(QtWidgets.QMainWindow, mainView.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        global args
        self.args = OdeArgs.OdeArgs()
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.printResultToListView)
        #S1
        self.S1.textChanged[str].connect(self.onS1Change)
        self.S1.textChanged[str].connect(self.checkOnEdit)
        #S2
        self.S2.textChanged[str].connect(self.onS2Change)
        self.S2.textChanged[str].connect(self.checkOnEdit)
        #K1
        self.alp1.textChanged[str].connect(self.onAlp1Change)
        self.alp1.textChanged[str].connect(self.checkOnEdit)
        #K2
        self.alp2.textChanged[str].connect(self.onAlp2Change)
        self.alp2.textChanged[str].connect(self.checkOnEdit)
        #alp1
        self.gam1.textChanged[str].connect(self.onGam1Change)
        self.gam1.textChanged[str].connect(self.checkOnEdit)
        #alp2
        self.gam2.textChanged[str].connect(self.onGam2Change)
        self.gam2.textChanged[str].connect(self.checkOnEdit)
        #gam1
        self.K1.textChanged[str].connect(self.onK1Change)
        self.K1.textChanged[str].connect(self.checkOnEdit)
        #gam2
        self.K2.textChanged[str].connect(self.onK2Change)
        self.K2.textChanged[str].connect(self.checkOnEdit)
        #Tn
        self.t0.textChanged[str].connect(self.onT0Change)
        self.t0.textChanged[str].connect(self.checkOnEdit)
        #T0
        self.tn.textChanged[str].connect(self.onTnChange)
        self.tn.textChanged[str].connect(self.checkOnEdit)

    def printResultToListView(self):
        self.listWidget.clear()
        _result = None
        try:
            ode_solver = OdeSolve.OdeSolve(self.args)
            _result = ode_solver.calc()
        except BaseException as e:
            print('printResultToListView exception: ' + str(e))

        for i in _result:
            self.listWidget.addItem(str(i))

    def onS1Change(self, text):
        self.listWidget.addItem('s1 = ' + str(text))
        try:
            self.args.set_s1(float(text))
        except BaseException as e:
            print(e)
    def onS2Change(self, text):
        self.listWidget.addItem('s2 = ' + str(text))
        try:
            self.args.set_s2(float(text))
        except BaseException as e:
            print(e)
    def onK1Change(self, text):
        self.listWidget.addItem('K1 = ' + str(text))
        try:
            self.args.set_k1(float(text))
        except BaseException as e:
            print(e)
    def onK2Change(self, text):
        self.listWidget.addItem('K2 = ' + str(text))
        try:
            self.args.set_k2(float(text))
        except BaseException as e:
            print(e)
    def onAlp1Change(self, text):
        self.listWidget.addItem('alp1 = ' + str(text))
        try:
            self.args.set_alp1(float(text))
        except BaseException as e:
            print(e)
    def onAlp2Change(self, text):
        self.listWidget.addItem('alp2 = ' + str(text))
        try:
            self.args.set_alp2(float(text))
        except BaseException as e:
            print(e)
    def onGam1Change(self, text):
        self.listWidget.addItem('gam1 = ' + str(text))
        try:
            self.args.set_gam1(float(text))
        except BaseException as e:
            print(e)
    def onGam2Change(self, text):
        self.listWidget.addItem('gam2 = ' + str(text))
        try:
            self.args.set_gam2(float(text))
        except BaseException as e:
            print(e)
    def onT0Change(self, text):
        self.listWidget.addItem('T0 = ' + str(text))
        try:
            self.args.set_t0(float(text))
        except BaseException as e:
            print(e)
    def onTnChange(self, text):
        self.listWidget.addItem('Tn = ' + str(text))
        try:
            self.args.set_tn(float(text))
        except BaseException as e:
            print(e)

    def checkOnEdit(self, input):
        args = [self.args.get_tn(), self.args.get_t0(), self.args.get_s1(), self.args.get_s2(), self.args.get_k1(),
                self.args.get_k2(), self.args.get_alp2(), self.args.get_alp1(), self.args.get_gam1(), self.args.get_gam2()]
        _i = 0
        for arg in args:
            if arg is not None:
                _i = _i+1

        if _i == 10:
            self.pushButton.setEnabled(True)

        try:
            _input = float(input)
            print(type(_input))
        except BaseException as e:
            print(e)
