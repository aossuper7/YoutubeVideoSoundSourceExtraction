from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

main = uic.loadUiType('View/MainWindows.ui')[0]


class MainWindows(QMainWindow, main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        QApplication(sys.argv).exec_()
