from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import re

Choice = uic.loadUiType('../View/ChoiceWindows.ui')[0]


class ChoiceWindow(QMainWindow, Choice):
    def __init__(self, parent, youtubeList, youtubeInfo, main, audioInfo):
        super().__init__(parent)
        self.setupUi(self)
        self.main = main
        self.youtube = youtubeList
        self.youtubeInfo = youtubeInfo
        self.audioInfo = audioInfo
        self.state = 0
        self.radioBtn = []
        self.audioBtn = []
        self.initUi()
        self.modifyUi()
        self.closebtn.clicked.connect(lambda: self.close())
        self.download.clicked.connect(lambda: self.downloadPictureEvent())
        self.comboBox.currentTextChanged.connect(lambda: self.modifyUi())
        self.save.clicked.connect(lambda: self.fileOpne())
        self.show()
        QApplication.processEvents()

    def initUi(self):
        self.setYoutubeInfo()
        self.setPictureList()
        self.setUiPicture()
        self.setAudioList()
        self.setUiAudio()

    def setYoutubeInfo(self):
        img = QPixmap()
        img.loadFromData(self.youtubeInfo['thumbnail'])
        self.image.setPixmap(img)
        self.title.setText(self.youtubeInfo['title'])
        self.time.setText(self.youtubeInfo['time'])
        self.url.setText('<a href=\"' + self.youtubeInfo['url'] + '\">' + self.youtubeInfo['url'] + '</a>')
        storage = os.path.expanduser('~') + '\Desktop\\' + self.youtubeInfo['title'] + '.mp4'
        self.storage.setText(self.modifiyFileName(storage))

    def setPictureList(self):
        Ysize = 0
        for youtube in self.youtube:
            label1 = QLabel(youtube[1], self.groupBox)
            label1.move(340, 12 + Ysize)
            label2 = QLabel(youtube[2], self.groupBox)
            label2.setGeometry(670, 12 + Ysize, 110, 21)
            label2.setAlignment(Qt.AlignRight)
            btn = QRadioButton(youtube[0].ljust(120), self.groupBox)
            btn.move(20, 10 + Ysize)
            btn.clicked.connect(lambda: self.setPictureStorage())
            Ysize += 40
            self.radioBtn.append(btn)

    def setAudioList(self):
        Ysize = 0
        for audio in self.audioInfo:
            label1 = QLabel(audio[1], self.groupBox_2)
            label1.move(270, 12 + Ysize)
            label2 = QLabel(audio[2], self.groupBox_2)
            label2.move(500, 12 + Ysize)
            label3 = QLabel(audio[3], self.groupBox_2)
            label3.move(720, 12 + Ysize)
            label3.setAlignment(Qt.AlignRight)
            btn = QRadioButton(audio[0].ljust(120), self.groupBox_2)
            btn.move(20, 10 + Ysize)
            btn.clicked.connect(lambda: self.setAudioStorage())
            Ysize += 40
            self.audioBtn.append(btn)

    def modifyUi(self):
        size = 0
        if self.state == 0:
            self.groupBox_2.hide()
            self.groupBox.show()
            size = len(self.youtube) * 40
            self.state = 1
        else:
            self.groupBox.hide()
            self.groupBox_2.show()
            size = len(self.audioInfo) * 40
            self.state = 0
        self.storage.move(20, 195 + size)
        self.save.move(660, 195 + size)
        self.closebtn.move(660, 240 + size)
        self.download.move(530, 240 + size)
        self.setFixedHeight(300 + size)

    def setUiPicture(self):
        size = len(self.youtube) * 40
        self.groupBox.setGeometry(0, 170, 791, 10 + size)

    def setUiAudio(self):
        size = len(self.audioInfo) * 40
        self.groupBox_2.setGeometry(0, 170, 791, 10 + size)

    def downloadPictureEvent(self):
        if self.state == 1:
            for i, radioBtn in enumerate(self.radioBtn):
                if radioBtn.isChecked():
                    self.main.downloadPictureEvent(i, self.storage.text())
                    return
        else:
            for i, radioBtn in enumerate(self.audioBtn):
                if radioBtn.isChecked():
                    self.main.downlaodAudioEvent(i, self.storage.text())
                    return

    def setPictureStorage(self):
        url = self.storage.text().split('.')
        url[1] = '.mp4'
        self.storage.setText(url[0] + url[1])

    def setAudioStorage(self):
        url = self.storage.text().split('.')
        for i, btn in enumerate(self.audioBtn):
            if btn.isChecked():
                url[1] = '.' + self.audioInfo[i][2]
                self.storage.setText(url[0] + url[1])
                return

    def fileOpne(self):
        fname = None
        if self.state == 1:
            fname = QFileDialog.getSaveFileName(self, filter='영상 (*.mp4)')
        else:
            fname = QFileDialog.getSaveFileName(self, filter='오디오 (*.webm *.mp4)')
        if fname[0]:
            self.storage.setText(fname[0].replace('/', '\\'))

    def modifiyFileName(self, names):
        name = names.split('\\')
        name[-1] = re.sub('[\/:*?"<>|]', ' ', name[-1])
        return '\\'.join(name)
