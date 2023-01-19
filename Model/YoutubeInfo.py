import pytube
import pyperclip

class YoutubeInfo:
    def __init__(self):
        self.checkLink()

    def checkLink(self):
        check = pytube.YouTube(pyperclip.paste())
        check.check_availability()