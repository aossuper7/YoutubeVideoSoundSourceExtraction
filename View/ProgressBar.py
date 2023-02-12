from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QCloseEvent, QMovie
from PyQt5.QtCore import QByteArray, QSize

ui = uic.loadUiType('../View/ProgressBar.ui')[0]


class Progressbar(QMainWindow, ui):
    def __init__(self, mainWindow, controller):
        super().__init__(mainWindow)
        self.setupUi(self)
        self.controller = controller
        self.startProgressBar()

    def startProgressBar(self):
        movie = QMovie('../Img/progressBar.gif', QByteArray(), self)
        movie.setCacheMode(QMovie.CacheAll)
        size = QSize(481, 31)
        movie.setScaledSize(size)
        movie.start()
        self.label.setMovie(movie)


    def closeEvent(self, a0: QCloseEvent) -> None:
        self.controller.stop_thread = True

