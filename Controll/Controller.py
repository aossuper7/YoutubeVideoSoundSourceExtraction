import View.MainWindow as MainWindow
import View.GetInfoWindow as GetInfoWindow
import View.ChoiceWindow as ChoiceWindow
from PyQt5.QtWidgets import QApplication
from Model import YoutubeMovieList, YoutubeInfoList, LoadingBar
import threading as th
import sys


class mainControll:
    def __init__(self):
        self.mainWindow = MainWindow.MainWindows(self)
        self.GetInfoWindow = None
        self.parent = None
        self.YoutubeMovieList = None
        self.YoutubeInfoList = None
        self.loadingBar = None
        self.eve = None

    def downloadClickEvent(self, parent):
        self.parent = parent
        self.GetInfoWindow = GetInfoWindow.GetInfo(self.parent, self)
        self.loadingBar = LoadingBar.loadingBar(self.GetInfoWindow)
        self.YoutubeMovieList = YoutubeMovieList.YoutubeInfo(self.GetInfoWindow, self)
        if self.YoutubeMovieList.checkLink():
            self.YoutubeInfoList = YoutubeInfoList.InfoList()
            self.eve = [th.Event(), th.Event()]
            th.Thread(target=self.YoutubeInfoList.setInfo, daemon=True).start()
            th.Thread(target=self.YoutubeMovieList.loadPictureList, args=(self.eve,), daemon=True).start()
            th.Thread(target=self.newWindow, args=(self.eve,), daemon=True).start()

    def newWindow(self, eve):
        eve[1].wait()
        if eve[0].is_set():
            return
        self.GetInfoWindow.close()
        choice = ChoiceWindow.ChoiceWindow(self.parent, self.YoutubeMovieList.getPictureInfo(),
                                           self.YoutubeInfoList.getInfo())

    def setLoading(self, value, time):
        self.loadingBar.setLoading(value, time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = mainControll()
    app.exec_()
