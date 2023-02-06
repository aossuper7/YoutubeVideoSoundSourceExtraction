from PyQt5.QtWidgets import QApplication
from Controll import Controller
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Controller.Controll()
    sys.exit(app.exec_())
