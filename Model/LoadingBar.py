from time import sleep


class loadingBar:
    def __init__(self, main, eve):
        self.value = 0
        self.main = main.mainWindow
        self.GetInfoWindow = main.GetInfoWindow
        self.eve = eve

    def setLoading(self, value, time):
        self.value += value
        for i in range(self.GetInfoWindow.progressBar.value(), self.value + 2):
            self.GetInfoWindow.progressBar.setValue(i)
            sleep(time)
            if self.eve.is_set():
                return

    def downloadLoading(self, chunk, file_handle, bytes_remaining, picture, num):
        progress = (100 * (picture[num].filesize - bytes_remaining)) / picture[num].filesize
        self.main.custom_widget.progressBar.setValue(progress)
