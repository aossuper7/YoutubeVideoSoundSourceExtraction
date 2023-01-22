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
        self.checkLink()

    def checkLink(self):
        try:
            self.youtube = pytube.YouTube(pyperclip.paste())
            self.youtube.check_availability()  # youtube 링크 체크
        except:
            QMessageBox.warning(self.youtubeInfoSearchWindow, '8k Youtube downloader', '잘못된 링크 입니다.')
            self.youtubeInfoSearchWindow.close()

    def loadPictureList(self):
        resolution = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p']
        Thread(target=self.main.loadingBar, args=(99, 0.13), daemon=True).start()
        for i in range(len(resolution)):
            youtube = self.youtube.streams\
                                    .filter(mime_type='video/mp4', progressive=False, res=resolution[i])\
                                    .order_by('mime_type')\
                                    .asc()
            if youtube is not None:
                self.picture.append(youtube)
        self.main.loadingBar(1, 0)

    def getPicture(self):
        return self.picture
