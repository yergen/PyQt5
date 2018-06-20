from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("paintEvent设置背景色")
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.yellow)
        #设置背景色
        painter.drawRect(self.rect())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
    
    
