import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("绘制矩形例子")
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()
    
    def initUI(self):
        #设置窗口大小600*500
        self.resize(600, 500)
        #设置画布大小为400*400，背景为白色
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
        
    #1
    def paintEvent(self, event):
        painter = QPainter(self)
        x = self.lastPoint.x()
        y = self.lastPoint.y()
        w = self.endPoint.x()-x
        h = self.endPoint.y()-y
        
        pp = QPainter(self.pix)
        #图形绘制在画布上
        pp.drawRect(x, y, w, h)
        #将画布绘制在窗口中
        painter.drawPixmap(0, 0, self.pix)
    
    #2
    def mousePressEvent(self, event):
        #按下鼠标左键
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
            
    #3
    def mouseMoveEvent(self, event):
        #然后移动鼠标指针
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            #进行重新绘制
            self.update()
        
    #4
    def mouseReleaseEvent(self, event):
        #释放鼠标左键
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            #进行重新绘制
            self.update()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
            
