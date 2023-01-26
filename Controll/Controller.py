import threading

import View.MainWindow as MainWindow
import View.GetInfoWindow as GetInfoWindow
import View.ChoiceWindow as ChoiceWindow
from PyQt5.QtWidgets import QApplication
from Model import YoutubeMovieList, YoutubeInfoList, LoadingBar
from threading import Thread
from time import sleep
import sys


class mainControll:
    def __init__(self):
        self.mainWindow = MainWindow.MainWindows(self)
        self.GetInfoWindow = None
        self.parent = None
        self.YoutubeMovieList = None
        self.YoutubeInfoList = None
        self.loadingBar = None

    def downloadClickEvent(self, parent):
        self.parent = parent
        self.GetInfoWindow = GetInfoWindow.GetInfo(self.parent)
        self.YoutubeMovieList = YoutubeMovieList.YoutubeInfo(self.GetInfoWindow, self)
        self.loadingBar = LoadingBar.loadingBar(self.GetInfoWindow)
        eve = threading.Event()
        if self.YoutubeMovieList.checkLink():
            self.YoutubeInfoList = YoutubeInfoList.InfoList()
            Thread(target=self.YoutubeInfoList.setInfo, daemon=True).start()
            Thread(target=self.YoutubeMovieList.loadPictureList, args=(eve,), daemon=True).start()
            Thread(target=self.newWindow, args=(eve,), daemon=True).start()

    def newWindow(self, eve):
        eve.wait()
        self.GetInfoWindow.close()
        choice = ChoiceWindow.ChoiceWindow(self.parent, self.YoutubeMovieList.getPictureInfo(),
                                           self.YoutubeInfoList.getInfo())

    def setLoading(self, value, time):
        self.loadingBar.setLoading(value, time)


    # def loadingBar(self, value, time):
    #     self.value += value
    #     for i in range(self.YoutubeInfoList.progressBar.value(), self.value + 1):
    #         self.YoutubeInfoList.progressBar.setValue(i)
    #         sleep(time)
    #
    #     if self.value == 100:
    #         self.value = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = mainControll()
    app.exec_()
