from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidget, QGridLayout, QWidget, QTableWidgetItem


def getBgColor(func_name: str):
    colors_dict = {
        "A1(t)": QColor(255, 255, 255),
        "A2(t)": QColor(204, 255, 255),
        "A3(t)": QColor(255, 255, 204),
        "A4(t)": QColor(205, 255, 204),
        "A5(t)": QColor(255, 204, 204),
    }
    return colors_dict[func_name]


class MapTable(QWidget):
    def __init__(self, accumulator):
        super().__init__()
        self.acc = accumulator
        self.setMinimumSize(QSize(1100, 800))
        self.setWindowTitle("Map")
        central_widget = QWidget(self)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        self.table = QTableWidget(self)
        self.table.setMinimumSize(1100, 800)
        self.table.setColumnCount(10)
        self.table.setRowCount(10)
        self.table.setHorizontalHeaderLabels(["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])
        self.table.setVerticalHeaderLabels(["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])

        grid_layout.addWidget(self.table, 0, 0)
        self.fillout()

    def fillout(self):
        i = 0
        j = 0
        for row in self.acc:
            at_arr = []
            for key, value in row:
                if str(key).startswith("A"):
                    at_arr.append((key, value))
            max_value = at_arr[0][1]
            max_key = at_arr[0][0]
            for key, value in at_arr:
                if max_value < value:
                    max_value = value
                    max_key = key
            self.table.setItem(i, j, QTableWidgetItem(str(max_key)))
            self.table.item(i, j).setBackground(getBgColor(str(max_key)))
            self.table.item(i, j).setToolTip(f"[{row[0][0]} = {row[0][1]}, {row[1][0]} = {row[1][1]}]")
            j += 1
            if j > 9:
                i += 1
                j = 0
