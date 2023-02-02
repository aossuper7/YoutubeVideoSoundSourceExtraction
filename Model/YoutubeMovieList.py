import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox
from threading import Thread
import multiprocessing as mp


class YoutubeInfo:

    def __init__(self, main):
        super().__init__()
        self.picture = []
        self.audioList = []
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
        t1 = Thread(target=self.main.setLoading, args=(99, 0.0005), daemon=True)
        t1.start()
        self.loadAudioList(eve)
        for resolution in resolutions:
            youtube = self.youtube.streams \
                .filter(mime_type='video/mp4', progressive=False, res=resolution) \
                .first()
            if eve.is_set():
                return
            if youtube:
                self.picture.append(youtube)
        t1.join()
        self.audio = self.youtube.streams.get_audio_only()
        self.main.setLoading(1)

    def loadAudioList(self, eve):
        audios = self.youtube.streams.filter(only_audio=True).order_by('abr').desc()
        for audio in audios:
            if eve.is_set():
                return
            self.audioList.append(audio)

    def downloadPicture(self, num, storage):
        fileName, storage = self.modifyStorage(storage)
        mp.Process(target=self.picture[num].download, args=(storage, 'video.mp4'), daemon=True).start()
        mp.Process(target=self.audio.download, args=(storage, 'audio.mp3'), daemon=True).start()

    def downloadAudio(self, num, storage):
        fileName, storage = self.modifyStorage(storage)
        mp.Process(target=self.audioList[num].download, args=(storage, fileName), daemon=True).start()

    def modifyStorage(self, storage):
        fileName = storage.split('/')
        storage = storage.replace(fileName[-1], '')
        return fileName[-1], storage

    def getPicture(self):
        return self.picture

    def getAudio(self):
        return self.audio

    def getAudioList(self):
        return self.audioList
