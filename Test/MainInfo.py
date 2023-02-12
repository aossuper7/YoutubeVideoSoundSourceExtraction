from unittest import TestCase
from Model import MainInfo
import pyperclip


class MainInfoTest(TestCase):
    def test_getTime(self):
        pyperclip.copy('https://www.youtube.com/watch?v=cKlEE_EYuNM')
        maininfo = MainInfo.MainInfo()
        maininfo.setTime()
        print(maininfo.time)