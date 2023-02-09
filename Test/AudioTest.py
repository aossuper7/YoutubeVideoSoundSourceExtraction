from unittest import TestCase
from Model import Audio
import pyperclip


class AudioTest(TestCase):
    def test_getAudioList(self):
        class temp:
            stop_thread = False

        pyperclip.copy('https://www.youtube.com/watch?v=qY22HPfafSQ')
        audioTest = Audio.Audio(temp)
        audioTest.makeAudioList()
        for audio in audioTest.audioList:
            print(audio)
