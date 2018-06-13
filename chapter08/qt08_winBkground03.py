from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    palette = QPalette()
    palette.setColor(QPalette.Background, Qt.red)
    win.setPalette(palette)
    win.show()
    sys.exit(app.exec_())
