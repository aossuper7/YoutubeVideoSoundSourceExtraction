from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem
from PyQt5.QtCore import *
from View import ListWidgetItem

main = uic.loadUiType('../View/MainWindows.ui')[0]


class MainWindows(QMainWindow, QObject, main):
    signal = pyqtSignal(object)

    def __init__(self, controller):
        super().__init__()
        QObject.__init__(self)
        self.setupUi(self)
        self.signal.connect(lambda: controller.downloadClickEvent(self))
        self.download.clicked.connect(lambda: self.signal.emit(self))
        self.show()
        self.custom_widget = None

    def downloadState(self, num, youtubeInfo, pictureInfo):
        item = QListWidgetItem()
        self.custom_widget = ListWidgetItem.addItem(num, youtubeInfo, pictureInfo)
        item.setSizeHint(QSize(500,100))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, self.custom_widget)
        self.listWidget.show()
