from unittest import TestCase
from Model import MainInfo
import pytube


class MainInfoTest(TestCase):
    def test_getTime(self):
        youtube = pytube.YouTube('https://www.youtube.com/watch?v=cKlEE_EYuNM')
        maininfo = MainInfo.MainInfo()
        maininfo.setTime(youtube)
        self.assertEqual(maininfo.time, '03:23')