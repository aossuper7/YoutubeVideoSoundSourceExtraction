import threading

import View.MainWindow as MainWindow
import View.GetInfoWindow as GetInfoWindow
import View.ChoiceWindow as ChoiceWindow
from PyQt5.QtWidgets import QApplication
from Model import YoutubeMovieList, YoutubeInfoList
from threading import Thread
from time import sleep
import sys


class mainControll:
    def __init__(self):
        self.mainWindow = MainWindow.MainWindows(self)
        self.info = None
        self.parent = None
        self.youtube = None
        self.youtubeInfo = None
        self.value = 0

    def downloadClickEvent(self, parent):
        self.parent = parent
        self.info = GetInfoWindow.GetInfo(self.parent)
        self.youtube = YoutubeMovieList.YoutubeInfo(self.info, self)
        eve = threading.Event()
        if self.youtube.checkLink():
            self.youtubeInfo = YoutubeInfoList.InfoList()
            Thread(target=self.youtubeInfo.setInfo, daemon=True).start()
            Thread(target=self.youtube.loadPictureList, args=(eve,), daemon=True).start()

        if eve.wait():
            self.info.close()
            choice = ChoiceWindow.ChoiceWindow(self.parent, self.youtube.getPictureInfo(),
                                               self.youtubeInfo.getInfo())

    def loadingBar(self, value, time):
        self.value += value
        for i in range(self.info.progressBar.value(), self.value + 1):
            self.info.progressBar.setValue(i)
            sleep(time)

        if self.value == 100:
            self.value = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = mainControll()
    app.exec_()
