

class AudioListInfo:
    audioList = []

    def __init__(self, audio):
        self.audio = audio
        self.getAudioList()

    def getAudioList(self):
        for audio in self.audio:
            self.audioList.append([self.getQuality(audio), audio.abr, str(round(audio.filesize_mb, 1)) + ' MB'])

    def getQuality(self, audio):
        quality = int(audio.abr[:-4])
        if quality >= 256:
            return '고음질'
        elif quality >= 128:
            return '일반 음질'
        else:
            return '저음질'
