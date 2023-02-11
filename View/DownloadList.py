from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

ui = uic.loadUiType('../View/DownloadList.ui')[0]


class MainWindow(QMainWindow, ui):
    def __init__(self, mainWindow, mainInfo):
        super().__init__(mainWindow)
        self.setupUi(self)
        self.show()
