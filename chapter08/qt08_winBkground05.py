from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("paintEvent设置背景色")
        
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./images/screen1.jpg")
        #设置窗口背景图片，平铺到整个窗口，随着窗口的改变而改变
        painter.drawPixmap(self.rect(), pixmap)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
    
    
