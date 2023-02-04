from time import sleep
import sys

class loadingBar:
    def __init__(self, main, eve):
        self.value = 0
        self.GetInfoWindow = main.GetInfoWindow
        self.eve = eve

    def setLoading(self, value, time):
        self.value += value
        for i in range(self.GetInfoWindow.progressBar.value(), self.value + 2):
            self.GetInfoWindow.progressBar.setValue(i)
            sleep(time)
            if self.eve.is_set():
                return

        if self.value == 100:
            self.value = 0
