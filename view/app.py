from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QTableWidgetItem

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
        self.setMinimumSize(QSize(920, 1080))
        self.ode_solver:OdeSolve.OdeSolve
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton.clicked.connect(self.onCalc)
        self.pushButton_2.clicked.connect(self.onBuildPlot)
        self.pushButton_3.clicked.connect(self.onExportClick)
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

    def onCalc(self):
        self.tableWidget.clear()
        _result = None
        _row_count = 0
        try:
            self.args.set_at(self.comboBox.currentText())
            self.ode_solver = OdeSolve.OdeSolve(self.args)
            _result = self.ode_solver.calc()
            _row_count = len(_result)
            self.tableWidget.setRowCount(_row_count)
        except BaseException as e:
            print('printResultToListView exception: ' + str(e))
        for i in range(_row_count):
            try:
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.ode_solver.getTimeline()[i])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(_result[i][0])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(_result[i][1])))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(_result[i][0]  + _result[i][1])))
            except BaseException as e:
                print('table fill exception'+str(e))
        self.pushButton_2.setEnabled(True)
        self.tableWidget.setHorizontalHeaderLabels(['t', 'K1', 'K2', 'K1+K2'])
        self.tableWidget.resizeColumnsToContents()

    def onBuildPlot(self):
        try:
            self.ode_solver.buildPlot()
        except BaseException as e:
            print(e)

    def onS1Change(self, text):
        try:
            self.args.set_s1(float(text))
        except BaseException as e:
            print(e)
    def onS2Change(self, text):
        try:
            self.args.set_s2(float(text))
        except BaseException as e:
            print(e)
    def onK1Change(self, text):
        try:
            self.args.set_k1(float(text))
        except BaseException as e:
            print(e)
    def onK2Change(self, text):
        try:
            self.args.set_k2(float(text))
        except BaseException as e:
            print(e)
    def onAlp1Change(self, text):
        try:
            self.args.set_alp1(float(text))
        except BaseException as e:
            print(e)
    def onAlp2Change(self, text):
        try:
            self.args.set_alp2(float(text))
        except BaseException as e:
            print(e)
    def onGam1Change(self, text):
        try:
            self.args.set_gam1(float(text))
        except BaseException as e:
            print(e)
    def onGam2Change(self, text):
        try:
            self.args.set_gam2(float(text))
        except BaseException as e:
            print(e)
    def onT0Change(self, text):
        try:
            self.args.set_t0(float(text))
        except BaseException as e:
            print(e)
    def onTnChange(self, text):
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

    def onExportClick(self):
        print(self.comboBox.currentText())
