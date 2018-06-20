from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/python.jpg")))
    win.setPalette(palette)
    win.resize(460, 255)
    win.show()
    sys.exit(app.exec_())
