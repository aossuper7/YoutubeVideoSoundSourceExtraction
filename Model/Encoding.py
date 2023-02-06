import os


class Encoding:
    def encodingPictureAudio(self, pictureName, audioName, fileName):
        command = f'ffmpeg -i {pictureName} -i {audioName} -c copy "{fileName}"'
        os.popen(command).read()
        os.remove(pictureName)
        os.remove(audioName)

    def __del__(self):
        print('encoding 제거')