class PictureListInfo:
    pictureList = []

    def __init__(self, picture, audio):
        self.picture = picture
        self.audio = audio
        self.getPictureList()

    def getPictureList(self):
        for picture in self.picture:
            self.pictureList.append([self.getResolutionGrade(picture), self.getResolution(picture),
                                     self.getFileSize(picture)])

    def getResolutionGrade(self, picture):
        resolution = int(picture.resolution[:-1])
        if resolution >= 2160:
            return '초고화질(UHD)'
        elif resolution >= 480:
            return '고화질'
        elif resolution >= 240:
            return '일반화질'
        else:
            return '저화질'

    def getResolution(self, picture):
        resolution = int(picture.resolution[:-1])
        resol = ''
        if resolution == 4320:
            resol += '8K ' + str(picture.fps) + 'fps' + self.getHDR(picture)
        elif resolution == 2160:
            resol += '4K ' + str(picture.fps) + 'fps' + self.getHDR(picture)
        elif resolution == 1440:
            resol += '2K ' + str(picture.fps) + 'fps' + self.getHDR(picture)
        else:
            resol += picture.resolution + ' ' + str(picture.fps) + 'fps'
        return resol

    def getHDR(self, picture):
        codec = picture.parse_codecs()[0].split('.')
        if len(codec) == 10:
            return ' HDR'
        else:
            return ''

    def getFileSize(self, picture):
        size = picture.filesize_mb + self.audio.filesize_mb
        if size >= 1024:
            return str(round(size/1024, 2)) + 'GB'
        else:
            return str(round(picture.filesize_mb, 1)) + 'MB'
