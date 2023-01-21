import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox


class YoutubeInfo:
    def __init__(self, youtubeInfoSearchWindow):
        self.picture = []
        self.youtube = None
        self.checkLink(youtubeInfoSearchWindow)

    def checkLink(self, youtubeInfoSearchWindow):
        try:
            self.youtube = pytube.YouTube(pyperclip.paste())
            self.youtube.check_availability()  # youtube 링크 체크
        except:
            QMessageBox.warning(youtubeInfoSearchWindow, '8k Youtube downloader', '잘못된 링크 입니다.')
            youtubeInfoSearchWindow.close()

    def loadPictureList(self):
        resolution = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p']
        for i in range(len(resolution)):
            youtube = self.youtube.streams\
                                    .filter(mime_type='video/mp4', progressive=False, res=resolution[i])\
                                    .order_by('mime_type')\
                                    .asc()
            if youtube is not None:
                self.picture.append(youtube)

    def getPicture(self):
        return self.picture
