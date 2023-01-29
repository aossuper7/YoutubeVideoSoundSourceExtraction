from time import sleep
import sys

class loadingBar:
    def __init__(self, main):
        self.value = 0
        self.GetInfoWindow = main.GetInfoWindow

    def setLoading(self, value, time):
        self.value += value
        for i in range(self.GetInfoWindow.progressBar.value(), self.value + 1):
            self.GetInfoWindow.progressBar.setValue(i)
            sleep(time)
        if self.value == 100:
            self.value = 0
