from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import threading

Choice = uic.loadUiType('../View/ChoiceWindows.ui')[0]


class ChoiceWindow(QMainWindow, Choice):
    def __init__(self, parent, youtubeList, youtubeInfo, main):
        super().__init__(parent)
        self.setupUi(self)
        self.main = main
        self.youtube = youtubeList
        self.youtubeInfo = youtubeInfo
        self.saveStorage = os.path.expanduser('~') + '\Desktop\\'
        self.setYoutubeInfo()
        self.radioBtn = []
        self.setList()
        self.modifyUi()
        self.closebtn.clicked.connect(lambda: self.close())
        self.download.clicked.connect(lambda: self.downloadEvent())
        self.show()
        QApplication.processEvents()

    def setYoutubeInfo(self):
        img = QPixmap()
        img.loadFromData(self.youtubeInfo['thumbnail'])
        self.image.setPixmap(img)
        self.title.setText(self.youtubeInfo['title'])
        self.time.setText(self.youtubeInfo['time'])
        self.url.setText('<a href=\"' + self.youtubeInfo['url'] + '\">' + self.youtubeInfo['url'] + '</a>')
        self.storage.setText(self.saveStorage + self.youtubeInfo['title'] + '.mp4')

    def setList(self):
        Ysize = 0
        for youtube in self.youtube:
            label1 = QLabel(youtube[1], self.groupBox)
            label1.move(340, 22 + Ysize)
            label2 = QLabel(youtube[2], self.groupBox)
            label2.setGeometry(670, 22 + Ysize, 110, 21)
            label2.setAlignment(Qt.AlignRight)
            btn = QRadioButton(youtube[0].ljust(120), self.groupBox)
            btn.move(20, 20 + Ysize)
            Ysize += 40
            self.radioBtn.append(btn)

    def modifyUi(self):
        size = len(self.youtube) * 40
        self.groupBox.setGeometry(0, 100, 791, 30 + size)
        self.storage.setGeometry(20, 145 + size, 621, 31)
        self.save.setGeometry(660, 145 + size, 112, 34)
        self.closebtn.setGeometry(660, 190 + size, 112, 34)
        self.download.setGeometry(530, 190 + size, 112, 34)
        self.setFixedHeight(250 + size)

    def downloadEvent(self):
        for i, radioBtn in enumerate(self.radioBtn):
            if radioBtn.isChecked():
                self.main.downloadEvent(i, self.saveStorage + '\Desktop\\')
