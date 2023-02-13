from unittest import TestCase
from Model import PictureListInfo
import pytube


class PictureListInfoTest(TestCase):
    def setUp(self) -> None:
        self.resolutions = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']
        self.moiveList = []
        self.moive = pytube.YouTube('https://www.youtube.com/watch?v=MyFPgkab6f4')
        self.audio = pytube.YouTube('https://www.youtube.com/watch?v=MyFPgkab6f4')
        self.audio = self.audio.streams.get_audio_only()

    def test_getPictureListInfo(self):
        for resolution in self.resolutions:
            temp = self.moive.streams.filter(mime_type='video/mp4', res=resolution).first()
            if temp:
                self.moiveList.append(temp)

        listInfo = PictureListInfo.PictureListInfo(self.moiveList, self.audio)
        print(listInfo.pictureList)