import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox
from threading import Thread


class YoutubeInfo:

    def __init__(self, main):
        super().__init__()
        self.picture = []
        self.youtube = None
        self.GetInfoWindow = main.GetInfoWindow
        self.main = main

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
        t1 = Thread(target=self.main.setLoading, args=(99, 0.12), daemon=True)
        t1.start()
        for i in range(len(resolution)):
            youtube = self.youtube.streams \
                .filter(mime_type='video/mp4', progressive=False, res=resolution[i]) \
                .first()
            if eve.is_set():
                return
            if youtube:
                self.picture.append(youtube)
        t1.join()
        self.main.setLoading(1)

    def getPicture(self):
        return self.picture
