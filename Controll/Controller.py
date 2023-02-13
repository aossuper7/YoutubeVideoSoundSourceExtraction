from PyQt5.QtWidgets import QApplication
from View import MainWindow, ProgressBar, DownloadList
from Model import Picture, Audio, MainInfo
from threading import Thread
from PyQt5.QtCore import QThread
import sys


class Controll:
    stop_thread = False  # 스레드 종료 변수

    def __init__(self):
        self.mainWindow = MainWindow.MainWindow(self)
        self.progressBar = ProgressBar.Progressbar(self.mainWindow, self)
        self.picture = Picture.Picture(self.mainWindow, self)
        self.audio = Audio.Audio(self)
        self.mainInfo = None
        self.makeMovieList = QThread()
        self.picture.moveToThread(self.makeMovieList)
        self.makeMovieList.started.connect(self.picture.makeMovieList)

    def downloadClickEvent(self):
        self.mainInfo = MainInfo.MainInfo()
        if self.picture.checkLink():
            self.progressBar.show()
            Thread(target=self.mainInfo.getInfo, daemon=True).start()
            self.makeMovieList.start()
            Thread(target=self.audio.makeAudioList, daemon=True).start()

    def showDownloadList(self):
        DownloadList.DownloadList(self.mainWindow, self.mainInfo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = Controll()
    sys.exit(app.exec_())
