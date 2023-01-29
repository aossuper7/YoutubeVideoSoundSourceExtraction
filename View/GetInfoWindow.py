from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QCloseEvent

second = uic.loadUiType('../View/GetInfoWindows.ui')[0]


class GetInfo(QMainWindow, second):
    def __init__(self, main):
        super().__init__(main.parent)
        self.setupUi(self)
        self.main = main
        self.show()
        QApplication.processEvents()

    def closeEvent(self, a0: QCloseEvent):
        if self.main.loadingBar.value != 0:
            self.main.eve.set()
