import pytube
import urllib.request
import pyperclip


class InfoList:
    def __init__(self):
        self.info = {}
        self.youtube = pytube.YouTube(pyperclip.paste())

    def setInfo(self):
        self.info['thumbnail'] = urllib.request.urlopen(self.youtube.thumbnail_url).read()
        self.info['title'] = self.youtube.title
        self.info['time'] = self.time()
        self.info['url'] = pyperclip.paste()

    def time(self):
        timeLength = self.youtube.length
        minutes = int(timeLength / 60)
        second = int(timeLength % 60)
        return str(minutes) + ":" + str(second)

    def getInfo(self):
        return self.info
