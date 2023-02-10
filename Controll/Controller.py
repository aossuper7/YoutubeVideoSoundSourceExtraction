from PyQt5.QtWidgets import QApplication
from View import MainWindow, ProgressBar
from Model import Picture, Audio
from threading import Thread
import sys


class Controll:
    stop_thread = False  # 스레드 종료 변수

    def __init__(self):
        self.mainWindow = MainWindow.MainWindow(self)
        self.progressBar = None
        self.picture = None
        self.audio = None

    def downloadClickEvent(self):
        self.picture = Picture.Picture(self.mainWindow, self)
        self.audio = Audio.Audio(self)
        self.progressBar = ProgressBar.Progressbar(self.mainWindow, self)
        if self.picture.checkLink():
            Thread(target=self.picture.makeMovieList, daemon=True).start()
            Thread(target=self.audio.makeAudioList, daemon=True).start()

    def setProgressBar(self, value, time = 0):
        t1 = Thread(target=self.progressBar.startProgressBar, args=(value, time), daemon=True)
        t1.start()
        return t1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = Controll()
    sys.exit(app.exec_())
