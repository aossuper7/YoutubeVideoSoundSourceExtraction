import pytube
import pyperclip


class Audio:
    def __init__(self, controller):
        self.audio = pytube.YouTube(pyperclip.paste())
        self.audioList = []
        self.controller = controller

    def makeAudioList(self):
        self.audio = self.audio.streams.filter(only_audio=True).order_by('abr').desc()
        for audio in self.audio:
            if self.controller.stop_thread:
                return
            self.audioList.append(audio)
