import urllib.request
import pytube
import pyperclip


class MainInfo:
    thumbnail = None
    title = None
    url = None
    time = ''

    def getInfo(self):
        picture = pytube.YouTube(pyperclip.paste())
        self.thumbnail = urllib.request.urlopen(picture.thumbnail_url).read()
        self.title = picture.title
        self.url = pyperclip.paste()
        self.setTime(picture)

    def setTime(self, time):
        time = time.length
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        if hours > 0:
            self.time += "{:d}:".format(int(hours))
        self.time += "{:02d}:{:02d}".format(int(minutes), int(seconds))
