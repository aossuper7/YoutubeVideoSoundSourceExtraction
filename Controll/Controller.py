import View.MainWindow as MainWindow
import View.GetInfoWindow as GetInfoWindow
from PyQt5.QtWidgets import QApplication
from Model import YoutubeInfo
from threading import Thread
import sys


class mainControll:
    def __init__(self):
        self.mainWindow = MainWindow.MainWindows()

    def downloadClickEvent(self, parent):
        info = GetInfoWindow.GetInfo(parent)
        youtube = YoutubeInfo.YoutubeInfo()

        t1 = Thread(target=youtube.checkLink, args=(info,))
        t1.daemon = True
        t1.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dd = mainControll()
    app.exec_()
