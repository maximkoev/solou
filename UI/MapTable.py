from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QTableWidget, QGridLayout, QWidget, QTableWidgetItem


class MapTable(QWidget):
    def __init__(self, accumulator):
        super().__init__()
        self.acc = accumulator
        self.setMinimumSize(QSize(1100, 800))  # Устанавливаем размеры
        self.setWindowTitle("Работа с QTableWidget")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет

        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет

        self.table = QTableWidget(self)  # Создаём таблицу
        self.table.setMinimumSize(1100, 800)
        self.table.setColumnCount(10)  # Устанавливаем три колонки
        self.table.setRowCount(10)  # и одну строку в таблице
        self.table.setItem(0, 0, QTableWidgetItem("test item"))
        self.table.setHorizontalHeaderLabels(["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])
        self.table.setVerticalHeaderLabels(["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])

        grid_layout.addWidget(self.table, 0, 0)  # Добавляем таблицу в сетку
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
            j += 1
            if j > 9:
                i += 1
                j = 0
