from time import sleep


class loadingBar:
    def __init__(self, youtubeInfoList):
        self.value = 0
        self.youtubeInfoList = youtubeInfoList

    def setLoading(self, value, time):
        self.value += value
        for i in range(self.youtubeInfoList.progressBar.value(), self.value + 1):
            self.youtubeInfoList.progressBar.setValue(i)
            sleep(time)

        if self.value == 100:
            self.value = 0