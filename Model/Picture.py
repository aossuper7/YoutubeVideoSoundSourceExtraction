import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox


class Picture:
    def __init__(self, mainWindow, controller):
        self.movieList = []
        self.mainWindow = mainWindow
        self.controller = controller
        self.movie = pytube.YouTube(pyperclip.paste())
        self.resolutions = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']

    def checkLink(self):
        try:
            self.movie.check_availability()
            return True
        except:
            QMessageBox.warning(self.mainWindow, '8k Youtube downlaoder', '잘못된 링크 입니다.')
            self.controller.progressBar.close()

    def makeMovieList(self):
        t1 = self.startProgressBar()
        for resolution in self.resolutions:
            movie = self.movie.streams.filter(mime_type='video/mp4', res=resolution).first()
            if self.controller.stop_thread:
                return
            if movie:
                self.movieList.append(movie)
        t1.join()

    def startProgressBar(self):
        return self.controller.setProgressBar(100, 0.005)
