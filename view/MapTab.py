from PyQt5.QtWidgets import QTableWidgetItem

from UI.MapTable import MapTable
from src.OdeSolve import OdeSolve

from model.OdeArgs import OdeArgs
from view.Tab import Tab
from PyQt5.QtCore import Qt



class MapTab(Tab):
    def __init__(self, ui):
        super().__init__(OdeArgs(), ui)
        self.ui = ui
        self.chbCount = 0
        self.disableAllGamAlp()
        self.ui.S1_2.textChanged[str].connect(self.onS1Change)
        self.ui.S2_2.textChanged[str].connect(self.onS2Change)
        self.ui.alp1_2.textChanged[str].connect(self.onAlp1Change)
        self.ui.alp2_2.textChanged[str].connect(self.onAlp2Change)
        self.ui.gam1_2.textChanged[str].connect(self.onGam1Change)
        self.ui.gam2_2.textChanged[str].connect(self.onGam2Change)
        self.ui.K1_2.textChanged[str].connect(self.onK1Change)
        self.ui.K2_2.textChanged[str].connect(self.onK2Change)
        self.ui.tn_2.textChanged[str].connect(self.onTnChange)
        self.ui.t0_2.setDisabled(True)
        self.ui.alp1_chb.stateChanged.connect(self.onChb)
        self.ui.alp2_chb.stateChanged.connect(self.onChb)
        self.ui.gam2_chb.stateChanged.connect(self.onChb)
        self.ui.gam1_chb.stateChanged.connect(self.onChb)
        self.ui.calc_mapper.setDisabled(True)
        self.ui.calc_mapper.clicked.connect(self.onCalc)
        self.ui.build_map.clicked.connect(self.onBuildMap)
        self.ui.build_map.setDisabled(True)
        self.alp_gam_array = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self.__set_fixed_arguments_list = []
        self.map_accumulator = []

    def onChb(self, state):
        if state == Qt.Checked:
            self.chbCount += 1
        else:
            self.chbCount -= 1
        if self.chbCount == 2:
            self.enableNotSelected()
        else:
            self.disableAllGamAlp()

    def onTnChange(self, text):
        self.onChange(text, self.args.set_t0)
        self.onChange(text, self.args.set_tn)

    def onCalc(self):
        __result = 0
        self.__redraw_table()
        self.__calculate()
        for argument in self.__set_fixed_arguments_list:
            argument(self.alp_gam_array[0])
        self.__fillout_table()
        self.ui.build_map.setDisabled(False)

    def enableNotSelected(self):
        self.__fixed_arguments_names = []
        chbstatusarr = [{"chb": self.ui.gam1_chb, "field": self.ui.gam1_2, "set": self.args.set_gam1, "name": "gam1"},
                        {"chb": self.ui.gam2_chb, "field": self.ui.gam2_2, "set": self.args.set_gam2, "name": "gam2"},
                        {"chb": self.ui.alp1_chb, "field": self.ui.alp1_2, "set": self.args.set_alp1, "name": "alp1"},
                        {"chb": self.ui.alp2_chb, "field": self.ui.alp2_2, "set": self.args.set_alp2, "name": "alp2"}]
        for checkbox in chbstatusarr:
            if checkbox["chb"].checkState() != Qt.Checked:
                checkbox["field"].setEnabled(True)
            else:
                checkbox['field'].clear()
                checkbox["set"](self.alp_gam_array[0])
                self.__set_fixed_arguments_list.append(checkbox["set"])
                self.__fixed_arguments_names.append(checkbox["name"])

    def disableAllGamAlp(self):
        self.ui.gam2_2.setDisabled(True)
        self.ui.gam1_2.setDisabled(True)
        self.ui.alp2_2.setDisabled(True)
        self.ui.alp1_2.setDisabled(True)

    def __calculate(self, ):
        __row = 0
        for i in self.alp_gam_array:
            self.__set_fixed_arguments_list[0](i)
            for j in self.alp_gam_array:
                self.__set_fixed_arguments_list[1](j)
                at_column = 2
                row_array = [(self.__fixed_arguments_names[0], i), (self.__fixed_arguments_names[1], j)]
                for at_function in self.args.get_at_keys():
                    self.args.set_at(at_function)
                    _r = OdeSolve(self.args).calc()
                    _r = _r[len(_r) - 1]
                    row_array.append((at_function, _r[0] + _r[1]))
                    at_column += 1
                self.__map_data_accumulator(row_array)
                __row += 1

    def __fillout_table(self):
        self.ui.map_table.setRowCount(len(self.map_accumulator))
        row_number = 0
        for row in self.map_accumulator:
            column_number = 0
            for key, value in row:
                self.ui.map_table.setItem(row_number, column_number, QTableWidgetItem(str(value)))
                column_number += 1
            row_number += 1

    def __redraw_table(self):
        self.ui.map_table.setColumnCount(7)
        self.ui.map_table.insertRow(0)
        self.ui.map_table.setHorizontalHeaderLabels([
            str(self.__fixed_arguments_names[0]),
            str(self.__fixed_arguments_names[1]),
            'P1+P2_A1', 'P1+P2_A2', 'P1+P2_A3', 'P1+P2_A4', 'P1+P2_A5'])

    def __map_data_accumulator(self, value):
        self.map_accumulator.append(value)

    def onBuildMap(self):
        try:
            mp = MapTable(self.map_accumulator)
            mp.show()
            mp.window().__init__(self.map_accumulator)
        except BaseException as e:
            print(e)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
