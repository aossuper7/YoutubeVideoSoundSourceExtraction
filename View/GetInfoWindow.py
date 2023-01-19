from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

second = uic.loadUiType('./GetInfoWindows.ui')[0]


class GetInfo(QMainWindow, second):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
