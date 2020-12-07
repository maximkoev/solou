from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QTableWidgetItem

from UI import mainView
from src import OdeSolve
from model import OdeArgs
from view.MapTab import MapTab
from view.PlotTab import PlotTab


class App(QtWidgets.QMainWindow, mainView.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.args = OdeArgs.OdeArgs()
        self.plotTab = PlotTab(self)
        self.mapTab = MapTab(self)
