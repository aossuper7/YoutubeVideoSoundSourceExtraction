import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox
from threading import Thread


class YoutubeInfo:
    def __init__(self, youtubeInfoSearchWindow, main):
        self.picture = []
        self.youtube = None
        self.youtubeInfoSearchWindow = youtubeInfoSearchWindow
        self.main = main

    def checkLink(self):
        try:
            self.youtube = pytube.YouTube(pyperclip.paste())
            self.youtube.check_availability()  # youtube 링크 체크
            return True
        except:
            QMessageBox.warning(self.youtubeInfoSearchWindow, '8k Youtube downloader', '잘못된 링크 입니다.')
            self.youtubeInfoSearchWindow.close()

    def loadPictureList(self, eve):
        resolution = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p']
        Thread(target=self.main.setLoading, args=(99, 0.13), daemon=True).start()
        for i in range(len(resolution)):
            youtube = self.youtube.streams \
                .filter(mime_type='video/mp4', progressive=False, res=resolution[i]) \
                .first()
            if youtube:
                self.picture.append(youtube)
        self.main.setLoading(1, 0.13)
        eve.set()

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
