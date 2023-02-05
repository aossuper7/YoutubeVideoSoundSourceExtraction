from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap


class addItem(QWidget):
    def __init__(self, num, youtubeInfo, pictureInfo):
        super().__init__()
        uic.loadUi('../View/ListWidgetItem.ui', self)
        img = QPixmap()
        img.loadFromData(youtubeInfo['thumbnail'])
        self.image.setPixmap(img)
        self.title.setText(youtubeInfo['title'])
        self.time.setText(youtubeInfo['time'])
        self.volume.setText(pictureInfo[num][2])
