from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

import Controll.Controller as Controller

main = uic.loadUiType('../View/MainWindows.ui')[0]


class MainWindows(QMainWindow, main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.download.clicked.connect(lambda: Controller.mainControll().downloadClickEvent(self))
        self.show()
