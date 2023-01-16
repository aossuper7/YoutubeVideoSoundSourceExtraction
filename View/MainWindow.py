import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from_class = uic.loadUiType("./MainWindows.ui")[0]

class MainWindows(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()
    window.show()
    app.exec_()