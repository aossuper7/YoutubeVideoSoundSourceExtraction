from PyQt5.QtWidgets import QApplication
import sys
from View import MainWindow, ProgressBar
from Model import YoutubeDownloader


class Controll:
    stop_thread = False  # 스레드 종료 변수

    def __init__(self):
        self.mainWindow = MainWindow.MainWindow(self)
        self.progressBar = ProgressBar.Progressbar(self.mainWindow, self)
        self.youtubeDownlaoder = YoutubeDownloader.YoutubeDownloader(self.mainWindow, self)

    def downloadClickEvent(self):
        if self.youtubeDownlaoder.checkLink():
            self.progressBar.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = Controll()
    sys.exit(app.exec_())
