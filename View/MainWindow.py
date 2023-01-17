import sys
import GetInfo
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

main = uic.loadUiType('./MainWindows.ui')[0]


class MainWindows(QMainWindow, main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.download.clicked.connect(self.downloadInfoWindows)
        self.show()

    def downloadInfoWindows(self):
        down = GetInfo.GetInfo(self)
        down.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()
    app.exec_()
