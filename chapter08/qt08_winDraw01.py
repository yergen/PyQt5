import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("绘图例子")
        #1
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()
    
    def initUI(self):
        #设置窗口大小为600*500
        self.resize(600, 500)
        #设置画布大小为400*400，背景为白色
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
        
    #2 
    def paintEvent(self, event):
        pp = QPainter(self.pix)
        #根据鼠标指针前后两个位置绘制直线
        pp.drawLine(self.lastPoint, self.endPoint)
        #让前一个坐标值等于后一个坐标值，就能画出连续的线
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)
    
    #3
    def mousePressEvent(self, event):
        #按下鼠标左键
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
    
    #4
    def mouseMoveEvent(self, event):
        #然后移动鼠标指针
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            #进行重新绘制
            self.update()
    
    #5
    def mouseReleaseEvent(self, event):
        #释放鼠标左键
        if event.button() == Qt.LeftButton:
            self.endPoint == event.pos()
            #进行重新绘制
            self.update()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
            
        
    
