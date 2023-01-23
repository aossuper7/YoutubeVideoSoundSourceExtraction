from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

Choice = uic.loadUiType('../View/ChoiceWindows.ui')[0]


class ChoiceWindow(QMainWindow, Choice):
    def __init__(self, parent, youtubeList, youtubeInfo):
        super().__init__(parent)
        self.setupUi(self)
        self.youtube = youtubeList
        self.youtubeInfo = youtubeInfo
        self.setYoutubeInfo()
        self.show()
        QApplication.processEvents()

    def setYoutubeInfo(self):
        img = QPixmap()
        img.loadFromData(self.youtubeInfo['thumbnail'])
        self.image.setPixmap(img)

        self.title.setText(self.youtubeInfo['title'])
        self.time.setText(self.youtubeInfo['time'])
        self.url.setText('<a href=\\\"'+self.youtubeInfo['url']+'\">'+self.youtubeInfo['url']+'</a>')
        self.url.setOpenExternalLinks(True)
