# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperKateUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setMaximumSize(QtCore.QSize(0, 0))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1920, 1080))
        self.tabWidget.setMaximumSize(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setMinimumSize(QtCore.QSize(1920, 1080))
        self.tab.setBaseSize(QtCore.QSize(1920, 0))
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(910, 10, 1000, 1020))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(1000, 1020))
        self.tableWidget.setMaximumSize(QtCore.QSize(0, 0))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setEnabled(True)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 850, 250))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QtCore.QSize(850, 250))
        self.label_24.setMaximumSize(QtCore.QSize(0, 0))
        self.label_24.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_24.setBaseSize(QtCore.QSize(0, 0))
        self.label_24.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_24.setLineWidth(2)
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("../diploma5/sys.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_24.setIndent(0)
        self.label_24.setObjectName("label_24")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(260, 600, 2, 2))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_30.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 930, 250, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(250, 90))
        self.pushButton_2.setMaximumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 930, 250, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(250, 90))
        self.pushButton.setMaximumSize(QtCore.QSize(0, 0))
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setAutoRepeatDelay(0)
        self.pushButton.setAutoRepeatInterval(0)
        self.pushButton.setObjectName("pushButton")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(560, 270, 320, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QtCore.QSize(320, 480))
        self.label_25.setMaximumSize(QtCore.QSize(0, 0))
        self.label_25.setFrameShape(QtWidgets.QFrame.Box)
        self.label_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_25.setLineWidth(2)
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("../diploma5/at.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(30, 280, 531, 481))
        self.widget.setObjectName("widget")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_14.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout_14.setSpacing(30)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.S1 = QtWidgets.QLineEdit(self.widget)
        self.S1.setMinimumSize(QtCore.QSize(0, 35))
        self.S1.setObjectName("S1")
        self.horizontalLayout_10.addWidget(self.S1)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.alp1 = QtWidgets.QLineEdit(self.widget)
        self.alp1.setMinimumSize(QtCore.QSize(0, 35))
        self.alp1.setObjectName("alp1")
        self.horizontalLayout_8.addWidget(self.alp1)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.gam1 = QtWidgets.QLineEdit(self.widget)
        self.gam1.setMinimumSize(QtCore.QSize(0, 35))
        self.gam1.setObjectName("gam1")
        self.horizontalLayout_7.addWidget(self.gam1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.K1 = QtWidgets.QLineEdit(self.widget)
        self.K1.setMinimumSize(QtCore.QSize(0, 35))
        self.K1.setText("")
        self.K1.setObjectName("K1")
        self.horizontalLayout_9.addWidget(self.K1)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.t0 = QtWidgets.QLineEdit(self.widget)
        self.t0.setMinimumSize(QtCore.QSize(0, 35))
        self.t0.setObjectName("t0")
        self.horizontalLayout_4.addWidget(self.t0)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_14.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.S2 = QtWidgets.QLineEdit(self.widget)
        self.S2.setMinimumSize(QtCore.QSize(0, 35))
        self.S2.setObjectName("S2")
        self.horizontalLayout_2.addWidget(self.S2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.alp2 = QtWidgets.QLineEdit(self.widget)
        self.alp2.setMinimumSize(QtCore.QSize(0, 35))
        self.alp2.setObjectName("alp2")
        self.horizontalLayout_3.addWidget(self.alp2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.gam2 = QtWidgets.QLineEdit(self.widget)
        self.gam2.setMinimumSize(QtCore.QSize(0, 35))
        self.gam2.setObjectName("gam2")
        self.horizontalLayout_6.addWidget(self.gam2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.K2 = QtWidgets.QLineEdit(self.widget)
        self.K2.setMinimumSize(QtCore.QSize(0, 35))
        self.K2.setObjectName("K2")
        self.horizontalLayout_5.addWidget(self.K2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tn = QtWidgets.QLineEdit(self.widget)
        self.tn.setMinimumSize(QtCore.QSize(0, 35))
        self.tn.setObjectName("tn")
        self.horizontalLayout.addWidget(self.tn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_14.addLayout(self.verticalLayout_3)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(30, 760, 851, 71))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line_2 = QtWidgets.QFrame(self.widget1)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_11 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_28.addWidget(self.label_11)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(250, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_28.addWidget(self.comboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_28)
        self.widget2 = QtWidgets.QWidget(self.tab)
        self.widget2.setGeometry(QtCore.QRect(30, 840, 851, 71))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line = QtWidgets.QFrame(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.STP_checkbox = QtWidgets.QCheckBox(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STP_checkbox.sizePolicy().hasHeightForWidth())
        self.STP_checkbox.setSizePolicy(sizePolicy)
        self.STP_checkbox.setMinimumSize(QtCore.QSize(0, 35))
        self.STP_checkbox.setText("")
        self.STP_checkbox.setObjectName("STP_checkbox")
        self.horizontalLayout_12.addWidget(self.STP_checkbox)
        self.label_33 = QtWidgets.QLabel(self.widget2)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_12.addWidget(self.label_33)
        self.label_23 = QtWidgets.QLabel(self.widget2)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_12.addWidget(self.label_23)
        self.STP = QtWidgets.QLineEdit(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STP.sizePolicy().hasHeightForWidth())
        self.STP.setSizePolicy(sizePolicy)
        self.STP.setMinimumSize(QtCore.QSize(70, 35))
        self.STP.setObjectName("STP")
        self.horizontalLayout_12.addWidget(self.STP)
        spacerItem = QtWidgets.QSpacerItem(210, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.line_4 = QtWidgets.QFrame(self.widget2)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setMinimumSize(QtCore.QSize(1920, 1080))
        self.tab_2.setObjectName("tab_2")
        self.map_table = QtWidgets.QTableWidget(self.tab_2)
        self.map_table.setGeometry(QtCore.QRect(910, 10, 1000, 1020))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_table.sizePolicy().hasHeightForWidth())
        self.map_table.setSizePolicy(sizePolicy)
        self.map_table.setMinimumSize(QtCore.QSize(1000, 1020))
        self.map_table.setMaximumSize(QtCore.QSize(0, 0))
        self.map_table.setFrameShape(QtWidgets.QFrame.Box)
        self.map_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.map_table.setLineWidth(1)
        self.map_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.map_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.map_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.map_table.setProperty("showDropIndicator", False)
        self.map_table.setDragDropOverwriteMode(False)
        self.map_table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.map_table.setAlternatingRowColors(True)
        self.map_table.setWordWrap(False)
        self.map_table.setObjectName("map_table")
        self.map_table.setColumnCount(5)
        self.map_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.map_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.map_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.map_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.map_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.map_table.setHorizontalHeaderItem(4, item)
        self.calc_mapper = QtWidgets.QPushButton(self.tab_2)
        self.calc_mapper.setGeometry(QtCore.QRect(30, 930, 250, 90))
        self.calc_mapper.setMinimumSize(QtCore.QSize(250, 90))
        self.calc_mapper.setObjectName("calc_mapper")
        self.build_map = QtWidgets.QPushButton(self.tab_2)
        self.build_map.setGeometry(QtCore.QRect(300, 930, 250, 90))
        self.build_map.setMinimumSize(QtCore.QSize(250, 90))
        self.build_map.setObjectName("build_map")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setEnabled(True)
        self.label_26.setGeometry(QtCore.QRect(10, 10, 850, 250))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(850, 250))
        self.label_26.setMaximumSize(QtCore.QSize(0, 0))
        self.label_26.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_26.setBaseSize(QtCore.QSize(0, 0))
        self.label_26.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_26.setLineWidth(2)
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("../diploma5/sys.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_26.setIndent(0)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(560, 270, 320, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QtCore.QSize(320, 480))
        self.label_27.setMaximumSize(QtCore.QSize(0, 0))
        self.label_27.setFrameShape(QtWidgets.QFrame.Box)
        self.label_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_27.setLineWidth(2)
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("../diploma5/at.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.widget3 = QtWidgets.QWidget(self.tab_2)
        self.widget3.setGeometry(QtCore.QRect(30, 280, 531, 481))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_17.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout_17.setSpacing(30)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.widget3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.S1_2 = QtWidgets.QLineEdit(self.widget3)
        self.S1_2.setObjectName("S1_2")
        self.horizontalLayout_11.addWidget(self.S1_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.alp1_chb = QtWidgets.QCheckBox(self.widget3)
        self.alp1_chb.setText("")
        self.alp1_chb.setObjectName("alp1_chb")
        self.horizontalLayout_18.addWidget(self.alp1_chb)
        self.label_14 = QtWidgets.QLabel(self.widget3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_18.addWidget(self.label_14)
        self.alp1_2 = QtWidgets.QLineEdit(self.widget3)
        self.alp1_2.setObjectName("alp1_2")
        self.horizontalLayout_18.addWidget(self.alp1_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.gam1_chb = QtWidgets.QCheckBox(self.widget3)
        self.gam1_chb.setText("")
        self.gam1_chb.setObjectName("gam1_chb")
        self.horizontalLayout_19.addWidget(self.gam1_chb)
        self.label_15 = QtWidgets.QLabel(self.widget3)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_19.addWidget(self.label_15)
        self.gam1_2 = QtWidgets.QLineEdit(self.widget3)
        self.gam1_2.setObjectName("gam1_2")
        self.horizontalLayout_19.addWidget(self.gam1_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_16 = QtWidgets.QLabel(self.widget3)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_20.addWidget(self.label_16)
        self.K1_2 = QtWidgets.QLineEdit(self.widget3)
        self.K1_2.setObjectName("K1_2")
        self.horizontalLayout_20.addWidget(self.K1_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_17 = QtWidgets.QLabel(self.widget3)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_21.addWidget(self.label_17)
        self.t0_2 = QtWidgets.QLineEdit(self.widget3)
        self.t0_2.setObjectName("t0_2")
        self.horizontalLayout_21.addWidget(self.t0_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_17.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_18 = QtWidgets.QLabel(self.widget3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_22.addWidget(self.label_18)
        self.S2_2 = QtWidgets.QLineEdit(self.widget3)
        self.S2_2.setObjectName("S2_2")
        self.horizontalLayout_22.addWidget(self.S2_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.alp2_chb = QtWidgets.QCheckBox(self.widget3)
        self.alp2_chb.setText("")
        self.alp2_chb.setObjectName("alp2_chb")
        self.horizontalLayout_23.addWidget(self.alp2_chb)
        self.label_19 = QtWidgets.QLabel(self.widget3)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_23.addWidget(self.label_19)
        self.alp2_2 = QtWidgets.QLineEdit(self.widget3)
        self.alp2_2.setObjectName("alp2_2")
        self.horizontalLayout_23.addWidget(self.alp2_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.gam2_chb = QtWidgets.QCheckBox(self.widget3)
        self.gam2_chb.setText("")
        self.gam2_chb.setObjectName("gam2_chb")
        self.horizontalLayout_24.addWidget(self.gam2_chb)
        self.label_20 = QtWidgets.QLabel(self.widget3)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_24.addWidget(self.label_20)
        self.gam2_2 = QtWidgets.QLineEdit(self.widget3)
        self.gam2_2.setObjectName("gam2_2")
        self.horizontalLayout_24.addWidget(self.gam2_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_21 = QtWidgets.QLabel(self.widget3)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_25.addWidget(self.label_21)
        self.K2_2 = QtWidgets.QLineEdit(self.widget3)
        self.K2_2.setObjectName("K2_2")
        self.horizontalLayout_25.addWidget(self.K2_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_22 = QtWidgets.QLabel(self.widget3)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_26.addWidget(self.label_22)
        self.tn_2 = QtWidgets.QLineEdit(self.widget3)
        self.tn_2.setObjectName("tn_2")
        self.horizontalLayout_26.addWidget(self.tn_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_17.addLayout(self.verticalLayout_4)
        self.widget4 = QtWidgets.QWidget(self.tab_2)
        self.widget4.setGeometry(QtCore.QRect(30, 840, 851, 73))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_3 = QtWidgets.QFrame(self.widget4)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_8.addWidget(self.line_3)
        self.STP_horizontal_2 = QtWidgets.QHBoxLayout()
        self.STP_horizontal_2.setObjectName("STP_horizontal_2")
        self.STP_checkbox_2 = QtWidgets.QCheckBox(self.widget4)
        self.STP_checkbox_2.setObjectName("STP_checkbox_2")
        self.STP_horizontal_2.addWidget(self.STP_checkbox_2)
        self.label_12 = QtWidgets.QLabel(self.widget4)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.STP_horizontal_2.addWidget(self.label_12)
        self.STP_2 = QtWidgets.QLineEdit(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STP_2.sizePolicy().hasHeightForWidth())
        self.STP_2.setSizePolicy(sizePolicy)
        self.STP_2.setMinimumSize(QtCore.QSize(70, 35))
        self.STP_2.setObjectName("STP_2")
        self.STP_horizontal_2.addWidget(self.STP_2)
        spacerItem1 = QtWidgets.QSpacerItem(210, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.STP_horizontal_2.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.STP_horizontal_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.line_5 = QtWidgets.QFrame(self.widget4)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_9.addWidget(self.line_5)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "t"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "P1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P1+P2"))
        self.pushButton_2.setText(_translate("MainWindow", "Build plot"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_10.setText(_translate("MainWindow", "S1"))
        self.label_8.setText(_translate("MainWindow", "alp1"))
        self.label_7.setText(_translate("MainWindow", "gam1"))
        self.label_9.setText(_translate("MainWindow", "K1"))
        self.label_4.setText(_translate("MainWindow", "t0"))
        self.label_2.setText(_translate("MainWindow", "S2"))
        self.label_3.setText(_translate("MainWindow", "alp2"))
        self.label_6.setText(_translate("MainWindow", "gam2"))
        self.label_5.setText(_translate("MainWindow", "K2"))
        self.label.setText(_translate("MainWindow", "tn"))
        self.label_11.setText(_translate("MainWindow", "A(t) = "))
        self.comboBox.setItemText(0, _translate("MainWindow", "A1(t)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "A2(t)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "A3(t)"))
        self.comboBox.setItemText(3, _translate("MainWindow", "A4(t)"))
        self.comboBox.setItemText(4, _translate("MainWindow", "A5(t)"))
        self.STP_checkbox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Take int account in calculation Since and Technical Progress</p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "Include STP in calculation"))
        self.label_23.setText(_translate("MainWindow", "δ ‎="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Plot"))
        item = self.map_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "P1+P2_A1"))
        item = self.map_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "P1+P2_A2"))
        item = self.map_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P1+P2_A3"))
        item = self.map_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P1+P2_A4"))
        item = self.map_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "P1+P2_A5"))
        self.calc_mapper.setText(_translate("MainWindow", "Calculate"))
        self.build_map.setText(_translate("MainWindow", "Build Map"))
        self.label_13.setText(_translate("MainWindow", "S1"))
        self.label_14.setText(_translate("MainWindow", "alp1"))
        self.label_15.setText(_translate("MainWindow", "gam1"))
        self.label_16.setText(_translate("MainWindow", "K1"))
        self.label_17.setText(_translate("MainWindow", "t0"))
        self.label_18.setText(_translate("MainWindow", "S2"))
        self.label_19.setText(_translate("MainWindow", "alp2"))
        self.label_20.setText(_translate("MainWindow", "gam2"))
        self.label_21.setText(_translate("MainWindow", "K2"))
        self.label_22.setText(_translate("MainWindow", "tn"))
        self.STP_checkbox_2.setText(_translate("MainWindow", "Include STP in calculation"))
        self.label_12.setText(_translate("MainWindow", "δ ‎="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Map"))
