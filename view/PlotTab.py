# from UI.mainView import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from model.OdeArgs import OdeArgs
from src.OdeSolve import OdeSolve
from view.Tab import Tab


class PlotTab(Tab):
    def __init__(self, ui):
        super().__init__(OdeArgs(), ui)
        self.__disableValuesOnStart()
        self.ui.pushButton.clicked.connect(self.onCalc)
        self.ui.pushButton_2.clicked.connect(self.onBuildPlot)
#        self.ui.pushButton_3.clicked.connect(self.onExportClick)
        self.ui.S1.textChanged[str].connect(self.onS1Change)
        self.ui.S2.textChanged[str].connect(self.onS2Change)
        self.ui.alp1.textChanged[str].connect(self.onAlp1Change)
        self.ui.alp2.textChanged[str].connect(self.onAlp2Change)
        self.ui.gam1.textChanged[str].connect(self.onGam1Change)
        self.ui.gam2.textChanged[str].connect(self.onGam2Change)
        self.ui.K1.textChanged[str].connect(self.onK1Change)
        self.ui.K2.textChanged[str].connect(self.onK2Change)
        self.ui.t0.textChanged[str].connect(self.onT0Change)
        self.ui.tn.textChanged[str].connect(self.onTnChange)
        self.ui.STP.textChanged[str].connect(self.onSTPChange)
        self.ui.STP_checkbox.stateChanged.connect(self.onSTPCheckbox)


    def onBuildPlot(self):
        try:
            self.ode_solver.buildPlot()
        except BaseException as e:
            print(e)

    def onExportClick(self):
        print(self.ui.comboBox.currentText())

    def onCalc(self):
        self.ui.tableWidget.clear()
        _result = None
        _row_count = 0
        try:
            self.args.set_at(self.ui.comboBox.currentText())
            self.ode_solver = OdeSolve(self.args)
            _result = self.ode_solver.calc()
            _row_count = len(_result)
            self.ui.tableWidget.setRowCount(_row_count)
        except BaseException as e:
            print('printResultToListView exception: ' + str(e))
        for i in range(_row_count):
            try:
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.ode_solver.getTimeline()[i])))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(_result[i][0])))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(_result[i][1])))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(_result[i][0] + _result[i][1])))
            except BaseException as e:
                print('table fill exception' + str(e))
        self.ui.pushButton_2.setEnabled(True)
        self.ui.tableWidget.setHorizontalHeaderLabels(['t', 'K1', 'K2', 'K1+K2'])
        self.ui.tableWidget.resizeColumnsToContents()

    def __disableValuesOnStart(self):
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton_2.setDisabled(True)
        self.ui.STP.setDisabled(True)

    def onSTPChange(self, text):
        self.onChange(text, self.args.set_STP)

    def onSTPCheckbox(self, state):
        if state == Qt.Checked:
            self.ui.STP.setEnabled(True)
        else:
            self.ui.STP.setDisabled(True)