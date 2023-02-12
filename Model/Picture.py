import pytube
import pyperclip
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *


class Picture(QObject):
    finished = pyqtSignal()

    def __init__(self, mainWindow, controller):
        super().__init__()
        self.movieList = []
        self.mainWindow = mainWindow
        self.controller = controller
        self.movie = None
        self.finished.connect(self.controller.showDownloadList)
        self.resolutions = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']

    def checkLink(self):
        try:
            self.movie = pytube.YouTube(pyperclip.paste())
            self.movie.check_availability()
            return True
        except:
            QMessageBox.warning(self.mainWindow, '8k Youtube downlaoder', '잘못된 링크 입니다.')

    def makeMovieList(self):
        for resolution in self.resolutions:
            movie = self.movie.streams.filter(mime_type='video/mp4', res=resolution).first()
            if self.controller.stop_thread:
                return
            if movie:
                self.movieList.append(movie)
        self.controller.progressBar.close()
        self.finished.emit()

    def getPicture(self):
        return self.movieList
