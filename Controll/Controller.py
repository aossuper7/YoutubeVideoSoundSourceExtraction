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
        self.value = 0

    def downloadClickEvent(self, parent):
        self.parent = parent
        self.info = GetInfoWindow.GetInfo(self.parent)
        youtube = YoutubeMovieList.YoutubeInfo(self.info, self)
        youtubeInfo = YoutubeInfoList.InfoList()
        Thread(target=youtubeInfo.setInfo, daemon=True).start()
        t1 = Thread(target=youtube.loadPictureList, daemon=True)
        t1.start()
        t1.join()
        self.info.close()
        choice = ChoiceWindow.ChoiceWindow(self.parent, youtube.getPictureInfo(), youtubeInfo.getInfo())

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
