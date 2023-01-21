import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox


class YoutubeInfo:
    def __init__(self):
        self.info = None
        self.youtube = None

    def checkLink(self, youtubeInfoSearchWindow):
        try:
            self.youtube = pytube.YouTube(pyperclip.paste())
            self.youtube.check_availability()  # youtube 링크 체크
        except:
            QMessageBox.warning(youtubeInfoSearchWindow, '8k Youtube downloader', '잘못된 링크 입니다.')
            youtubeInfoSearchWindow.close()

    def saveYoutubeInfo(self):
        self.info = self.youtube.streams
