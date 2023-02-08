from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

ui = uic.loadUiType('../View/MainWindow.ui')[0]


class MainWindow(QMainWindow, ui):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.download.clicked.connect(lambda: main.downloadClickEvent())
        self.show()
