from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QCloseEvent
from time import sleep

ui = uic.loadUiType('../View/ProgressBar.ui')[0]


class Progressbar(QMainWindow, ui):
    def __init__(self, mainWindow, controller):
        super().__init__(mainWindow)
        self.setupUi(self)
        self.controller = controller
        self.value = 0

    def startProgressBar(self, value, time):
        self.value = value
        for i in range(self.progressBar.value(), self.value + 2):
            if self.controller.stop_thread:
                return
            self.progressBar.setValue(i)
            sleep(time)

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.controller.stop_thread = True
