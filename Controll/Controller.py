from PyQt5.QtWidgets import QApplication
from View import MainWindow, ProgressBar
from Model import Picture, Audio, MainInfo
from threading import Thread
import sys


class Controll:
    stop_thread = False  # 스레드 종료 변수

    def __init__(self):
        self.mainWindow = MainWindow.MainWindow(self)
        self.progressBar = ProgressBar.Progressbar(self.mainWindow, self)
        self.picture = Picture.Picture(self.mainWindow, self)
        self.audio = Audio.Audio(self)
        self.mainInfo = None

    def downloadClickEvent(self):
        self.progressBar.show()
        QApplication.processEvents()
        if self.picture.checkLink():
            Thread(target=self.picture.makeMovieList, daemon=True).start()
            Thread(target=self.audio.makeAudioList, daemon=True).start()

    def makeMainInfo(self, picture):
        self.mainInfo = MainInfo.MainInfo(picture)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = Controll()
    sys.exit(app.exec_())
