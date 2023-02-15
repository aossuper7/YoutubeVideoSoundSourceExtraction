from unittest import TestCase
from Model import AudioListInfo
import pytube


class AudioListInfoTest(TestCase):
    def setUp(self) -> None:
        self.audio = pytube.YouTube('https://www.youtube.com/watch?v=rRzxEiBLQCA')
        self.audio = self.audio.streams.filter(only_audio=True).order_by('abr').desc()
        self.audioList = []
        for audio in self.audio:
            self.audioList.append(audio)

    def test_getAudioList(self):
        audio = AudioListInfo.AudioListInfo(self.audioList)
        print(audio.audioList)
