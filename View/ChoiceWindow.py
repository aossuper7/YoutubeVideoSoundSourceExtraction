from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

Choice = uic.loadUiType('../View/ChoiceWindows.ui')[0]


class ChoiceWindow(QMainWindow, Choice):
    def __init__(self, parent, youtubeList, youtubeInfo):
        super().__init__(parent)
        self.setupUi(self)
        self.youtube = youtubeList
        self.youtubeInfo = youtubeInfo
        self.saveStorage = os.path.expanduser('~')
        self.setYoutubeInfo()
        self.setList()
        self.show()
        QApplication.processEvents()

    def setYoutubeInfo(self):
        img = QPixmap()
        img.loadFromData(self.youtubeInfo['thumbnail'])
        self.image.setPixmap(img)
        self.title.setText(self.youtubeInfo['title'])
        self.time.setText(self.youtubeInfo['time'])
        self.url.setText('<a href=\"' + self.youtubeInfo['url'] + '\">' + self.youtubeInfo['url'] + '</a>')
        self.storage.setText(self.saveStorage + 'Desktop' + self.youtubeInfo['title'] + '.mp4')

    def setList(self):
        Ysize = 0
        for i in range(len(self.youtube)):
            label1 = QLabel(self.youtube[i][1], self.groupBox)
            label1.move(340, 22+Ysize)
            label2 = QLabel(self.youtube[i][2], self.groupBox)
            label2.setGeometry(670, 22+Ysize, 110, 21)
            label2.setAlignment(Qt.AlignRight)
            btn = QRadioButton(self.youtube[i][0].ljust(120), self.groupBox)
            btn.move(20, 20 + Ysize)
            Ysize += 40
