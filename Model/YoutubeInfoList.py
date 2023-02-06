import pytube
import urllib.request
import pyperclip
import re
from PyQt5.QtCore import *
from threading import Thread


class InfoList(QObject):
    signal = pyqtSignal()

    def __init__(self, main):
        super().__init__()
        self.info = {}
        self.youtube = pytube.YouTube(pyperclip.paste())
        self.videoInfo = []
        self.audioInfo = []
        self.signal.connect(lambda: main.newWindow())

    def setInfo(self, picture, audio, audioList):
        self.info['thumbnail'] = urllib.request.urlopen(self.youtube.thumbnail_url).read()
        self.info['title'] = self.youtube.title
        self.info['time'] = self.time()
        self.info['url'] = pyperclip.paste()

        t1 = Thread(target=self.savePictureInfo, args=(picture, audio.filesize_mb), daemon=True)
        t2 = Thread(target=self.saveAudioInfo, args=(audioList,), daemon=True)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        self.signal.emit()

    def time(self):
        timeLength = self.youtube.length
        minutes = int(timeLength / 60)
        second = int(timeLength % 60)
        return str(minutes) + ":" + str(second)

    def getInfo(self):
        return self.info

    def getPictureInfo(self):
        return self.videoInfo

    def savePictureInfo(self, pictures, audioSize):
        for picture in pictures:
            self.videoInfo.append([self.distinguishResolution(picture),
                                   picture.resolution + ' ' + str(picture.fps) + 'fps',
                                   str(round(picture.filesize_mb + audioSize, 1)) + 'MB'])

    def saveAudioInfo(self, audios):
        for audio in audios:
            type = audio.mime_type.split('/')
            self.audioInfo.append([self.distinguishSound(audio), audio.abr, type[1],
                                   str(round(audio.filesize_mb, 1)) + 'MB'])

    def getAudioInfo(self):
        return self.audioInfo

    def distinguishResolution(self, picture):
        resolution = int(picture.resolution[:-1])
        if resolution >= 2160:
            return '초고화질(UHD)'
        elif resolution >= 480:
            return '고화질'
        elif resolution >= 240:
            return '일반 화질'

    def distinguishSound(self, audio):
        numbers = int(re.sub(r'[^0-9]', '', audio.abr))
        if numbers >= 256:
            return '고음질'
        elif numbers >= 112:
            return '일반음질'
        else:
            return '저음질'

    def __del__(self):
        print('youtubeInfoList 제거')

