from unittest import TestCase
from Model import Picture
import pyperclip
import pytube


class PictureTest(TestCase):
    def test_getMovieList(self):
        class temp:
            stop_thread = False
        pyperclip.copy('https://www.youtube.com/watch?v=qY22HPfafSQ')
        picture = Picture.Picture('empty', temp)
        picture.makeMovieList()
        for movie in picture.movieList:
            print(movie)
