import View.MainWindow as MainWindow
import View.GetInfoWindow as GetInfoWindow
from PyQt5.QtWidgets import QApplication
from Model import YoutubeInfo
from threading import Thread
from time import sleep
import sys


class mainControll:
    def __init__(self):
        self.mainWindow = MainWindow.MainWindows(self)
        self.info = None
        self.value = 0

    def downloadClickEvent(self, parent):
        self.info = GetInfoWindow.GetInfo(parent)
        youtube = YoutubeInfo.YoutubeInfo(self.info, self)
        Thread(target=youtube.loadPictureList, daemon=True).start()

    def loadingBar(self, value, time):
        self.value += value
        for i in range(self.info.progressBar.value(), self.value + 1):
            self.info.progressBar.setValue(i)
            sleep(time)

        if self.value == 100:
            self.info.close()
            self.value = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = mainControll()
    app.exec_()
