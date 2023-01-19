from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Model import YoutubeInfo

second = uic.loadUiType('./GetInfoWindows.ui')[0]


class GetInfo(QMainWindow, second):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.show()
        self.getYoutubeInfo()

    def getYoutubeInfo(self):
        try:
            YoutubeInfo.YoutubeInfo()
        except:
            self.close()
            QMessageBox.warning(self, 'Youtube Downloader', '지원하지 않는 사이트 입니다.')
