import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox
from threading import Thread


class YoutubeDownloader:
    def __init__(self, mainWindow, controller):
        self.movie = None
        self.audio = None
        self.mainWindow = mainWindow
        self.controller = controller
        self.progressBar = controller.progressBar
        self.movieList = []
        self.audioList = None
        self.audioFirst = None

    def checkLink(self):
        try:
            url = pyperclip.paste()
            self.movie = [pytube.YouTube(url), pytube.YouTube(url)]  # 0: Movie, 1: audio
            self.audio = pytube.YouTube(url)
            self.movie[0].check_availability()
            return True
        except:
            QMessageBox.warning(self.mainWindow, '8K Youtube downloader', '잘못된 링크 입니다.')

    def makeMovieList(self):
        resolutions = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']
        Thread(target=self.makeAudio, daemon=True).start()
        Thread(target=self.makeAudioList, daemon=True).start()
        Thread(target=self.progressBar.startProgressBar, args=(100, 0.0005), daemon=True).start()
        for resolution in resolutions:
            MovieList = self.movie.streams.filter(mime_type='video/mp4', res=resolution).first()
            if self.controller.stop_thread:
                return
            if MovieList:
                self.movieList.append(MovieList)

    def makeAudio(self):
        self.audioFirst = self.movie[1].get_audio_only()

    def getMovieList(self):
        return self.movieList

    def makeAudioList(self):
        self.audioList = self.audio.stream.filter(only_audio=True).order_by('abr').desc()

    def getAudioList(self):
        return self.audioList
