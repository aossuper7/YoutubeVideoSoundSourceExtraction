from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap

ui = uic.loadUiType('../View/DownloadList.ui')[0]


class DownloadList(QMainWindow, ui):
    def __init__(self, mainWindow, mainInfo):
        super().__init__(mainWindow)
        self.mainInfo = mainInfo
        self.setupUi(self)
        self.setMainInfo()
        self.cancelBtn.clicked.connect(lambda: self.close())
        self.show()

    def setMainInfo(self):
        pixmap = QPixmap()
        pixmap.loadFromData(self.mainInfo.thumbnail)
        self.thumbnail.setPixmap(pixmap)
        self.thumbnail.setScaledContents(True)
        self.title.setText(self.mainInfo.title)
        self.time.setText(self.mainInfo.time)
        self.link.setText('<a href="'+self.mainInfo.url+'">'+self.mainInfo.url+'</a>')
