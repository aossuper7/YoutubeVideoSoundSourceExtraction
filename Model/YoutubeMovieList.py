import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox
from threading import Thread
import multiprocessing as mp


class YoutubeInfo:

    def __init__(self, main):
        super().__init__()
        self.picture = []
        self.audio = None
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
        resolutions = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p']
        t1 = Thread(target=self.main.setLoading, args=(99, 0.005), daemon=True)
        t1.start()
        for resolution in resolutions:
            youtube = self.youtube.streams \
                .filter(mime_type='video/mp4', progressive=False, res=resolution) \
                .first()
            if eve.is_set():
                return
            if youtube:
                self.picture.append(youtube)
        self.audio = self.youtube.streams.get_audio_only()
        t1.join()
        self.main.setLoading(1)

    def downloadPicture(self, num, storage):
        mp.Process(target=self.picture[num].download, args=(storage, 'video.mp4'), daemon=True).start()
        mp.Process(target=self.audio.download, args=(storage, 'audio.mp3'), daemon=True).start()

    def getPicture(self):
        return self.picture

    def getAudio(self):
        return self.audio
