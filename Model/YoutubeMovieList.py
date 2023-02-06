import multiprocessing

import pytube
import pyperclip
from Model import Encoding
from PyQt5.QtWidgets import QMessageBox
from threading import Thread
from multiprocessing import Process


class YoutubeInfo:
    def __init__(self, main):
        self.picture = []
        self.audioList = []
        self.audio = None
        self.youtubeMovie = None
        self.youtubeAudio = None
        self.GetInfoWindow = main.GetInfoWindow
        self.main = main
        self.num = None
        self.fileName = None
        self.storage = None

    def checkLink(self, loading, encoding):
        try:
            self.youtubeMovie = pytube.YouTube(pyperclip.paste())
            self.youtubeAudio = pytube.YouTube(pyperclip.paste())
            self.youtubeMovie.register_on_progress_callback(loading)
            self.youtubeMovie.register_on_complete_callback(encoding)
            self.youtubeMovie.check_availability()  # youtube 링크 체크
            return True
        except:
            QMessageBox.warning(self.GetInfoWindow, '8k Youtube downloader', '잘못된 링크 입니다.')
            self.GetInfoWindow.close()

    def loadPictureList(self, eve):
        resolutions = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p']
        Thread(target=self.main.setLoading, args=(100,0.0005), daemon=True).start()
        t1 = Thread(target=self.temp, daemon=True)
        t2 = Thread(target=self.loadAudioList, args=(eve,), daemon=True)
        t1.start()
        t2.start()
        # self.loadAudioList(eve)
        for resolution in resolutions:
            youtube = self.youtubeMovie.streams \
                .filter(mime_type='video/mp4', progressive=False, res=resolution) \
                .first()
            if eve.is_set():
                return
            if youtube:
                self.picture.append(youtube)
        t1.join()
        t2.join()

    def temp(self):
        self.audio = self.youtubeAudio.streams.get_audio_only()

    def loadAudioList(self, eve):
        audios = self.youtubeAudio.streams.filter(only_audio=True).order_by('abr').desc()
        for audio in audios:
            if eve.is_set():
                return
            self.audioList.append(audio)

    def downloadPicture(self, num, storage):
        self.fileName, self.storage = self.modifyStorage(storage)
        self.num = num
        num_cores = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(num_cores)
        pool.map(self.picture[num].download, [self.storage, 'video'])
        pool.map(self.audio.download, [self.storage, 'audio'])
        # Process(target=self.picture[num].download, args=(self.storage, 'video'), daemon=True).start()
        # Process(target=self.audio.download, args=(self.storage, 'audio'), daemon=True).start()

    def downloadAudio(self, num, storage):
        fileName, storage = self.modifyStorage(storage)
        Thread(target=self.audioList[num].download, args=(storage, fileName), daemon=True).start()

    def modifyStorage(self, storage):
        fileName = storage.split('\\')
        storage = storage.replace(fileName[-1], '')
        return fileName[-1], storage

    def getPicture(self):
        return self.picture

    def getAudio(self):
        return self.audio

    def getAudioList(self):
        return self.audioList
