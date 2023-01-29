import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from threading import Thread


class YoutubeInfo(QObject):
    signal = pyqtSignal()

    def __init__(self, main):
        super().__init__()
        self.picture = []
        self.youtube = None
        self.GetInfoWindow = main.GetInfoWindow
        self.main = main
        self.signal.connect(lambda: main.newWindow())

    def checkLink(self):
        try:
            self.youtube = pytube.YouTube(pyperclip.paste())
            self.youtube.check_availability()  # youtube 링크 체크
            return True
        except:
            QMessageBox.warning(self.GetInfoWindow, '8k Youtube downloader', '잘못된 링크 입니다.')
            self.GetInfoWindow.close()

    def loadPictureList(self, eve):
        resolution = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p']
        Thread(target=self.main.setLoading, args=(99, 0.13), daemon=True).start()
        for i in range(len(resolution)):
            youtube = self.youtube.streams \
                .filter(mime_type='video/mp4', progressive=False, res=resolution[i]) \
                .first()
            if eve.is_set():
                return
            if youtube:
                self.picture.append(youtube)
        self.main.setLoading(1, 0.13)
        self.signal.emit()

    def getPictureInfo(self):
        videoInfo = []
        for i in range(len(self.picture)):
            videoInfo.append([self.distinguishResolution(self.picture[i]),
                              self.picture[i].resolution + ' ' + str(self.picture[i].fps) + 'fps',
                              str(round(self.picture[i].filesize_mb, 1)) + 'MB'])
        return videoInfo

    def distinguishResolution(self, youtube):
        resolution = int(youtube.resolution[:-1])
        if resolution >= 480:
            return '고화질'
        elif resolution >= 240:
            return '일반 화질'
