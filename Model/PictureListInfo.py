

class PictureListInfo:
    pictureList = []

    def __init__(self, picture, audio):
        self.picture = picture
        self.audio = audio

    def getResolutionGrade(self, picture):
        resolution = picture.resolution[:-1]
        if resolution >= 2160:
            return '초고화질(UHD)'
        elif resolution >= 480:
            return '고화질'
        elif resolution >= 240:
            return '일반화질'
        else:
            return '저화질'

    def getResolution(self, picture):
        resolution = picture.resolution[:-1]
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

    def getfilesize(self, picture):
        size = picture.filesize_mb + self.audio.filesize_mb
        if size >= 1024:
            return round(size/1024, 2)
        else:
            return picture.filesize_mb
