import pytube
import urllib.request
import pyperclip
from PyQt5.QtCore import *


class InfoList(QObject):
    signal = pyqtSignal()

    def __init__(self, main):
        super().__init__()
        self.info = {}
        self.youtube = pytube.YouTube(pyperclip.paste())
        self.videoInfo = []
        self.signal.connect(lambda: main.newWindow())

    def setInfo(self, picture):
        self.info['thumbnail'] = urllib.request.urlopen(self.youtube.thumbnail_url).read()
        self.info['title'] = self.youtube.title
        self.info['time'] = self.time()
        self.info['url'] = pyperclip.paste()
        self.savePictureInfo(picture)
        self.signal.emit()

    def time(self):
        timeLength = self.youtube.length
        minutes = int(timeLength / 60)
        second = int(timeLength % 60)
        return str(minutes) + ":" + str(second)

    def getInfo(self):
        return self.info

    def getPictureInfo(self):
        return self.videoInfo

    def savePictureInfo(self, picture):
        for i in range(len(picture)):
            self.videoInfo.append([self.distinguishResolution(picture[i]),
                                   picture[i].resolution + ' ' + str(picture[i].fps) + 'fps',
                                   str(round(picture[i].filesize_mb, 1)) + 'MB'])

    def distinguishResolution(self, picture):
        resolution = int(picture.resolution[:-1])
        if resolution >= 2160:
            return '초고화질(UHD)'
        elif resolution >= 480:
            return '고화질'
        elif resolution >= 240:
            return '일반 화질'
