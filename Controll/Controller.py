import View.MainWindow as MainWindow
import View.GetInfoWindow as GetInfoWindow
import View.ChoiceWindow as ChoiceWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
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
        self.GetInfoWindow = GetInfoWindow.GetInfo(self)
        self.eve = th.Event()
        self.loadingBar = LoadingBar.loadingBar(self, self.eve)
        self.YoutubeMovieList = YoutubeMovieList.YoutubeInfo(self)
        if self.YoutubeMovieList.checkLink():
            self.YoutubeInfoList = YoutubeInfoList.InfoList(self)
            th.Thread(target=self.saveYoutube, daemon=True).start()

    @pyqtSlot()
    def newWindow(self):
        self.GetInfoWindow.close()
        choice = ChoiceWindow.ChoiceWindow(self.parent, self.YoutubeInfoList.getPictureInfo(),
                                           self.YoutubeInfoList.getInfo(), self)

    def setLoading(self, value, time=0):
        self.loadingBar.setLoading(value, time)

    def saveYoutube(self):
        self.YoutubeMovieList.loadPictureList(self.eve)
        if self.eve.is_set():
            return
        self.YoutubeInfoList.setInfo(self.YoutubeMovieList.getPicture())

    def downloadEvent(self, num, storage):
        th.Thread(target=self.YoutubeMovieList.downloadPicture, args=(num, storage), daemon=True).start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = mainControll()
    sys.exit(app.exec_())
