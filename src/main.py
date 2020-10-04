import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from view.app import App


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса App
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


main()
