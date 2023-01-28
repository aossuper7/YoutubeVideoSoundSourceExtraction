from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QCloseEvent
import os

main = uic.loadUiType('../View/MainWindows.ui')[0]


class MainWindows(QMainWindow, main):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.download.clicked.connect(lambda: controller.downloadClickEvent(self))
        self.show()

    def closeEvent(self, a0: QCloseEvent) -> None:
        pid = os.getpid()
        os.kill(pid, 2)
