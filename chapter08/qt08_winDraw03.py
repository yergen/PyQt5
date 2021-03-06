import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("双缓冲绘图例子")
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        #1
        #辅助画布
        self.tempPix = QPixmap()
        #标志是否正在绘制
        self.isDrawing = False
        self.initUi()
    
    def initUi(self):
        #设置窗口大小为600*500
        self.resize(600, 500)
        #设置画布大小为400*400，背景为白色
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
    
    #2
    def paintEvent(self, event):
        painter = QPainter(self)
        x = self.lastPoint.x()
        y = self.lastPoint.y()
        w = self.endPoint.x()-x
        h = self.endPoint.y()-y
        
        #如果正在绘图，就在辅助画布上绘制
        if self.isDrawing:
            #将以前pix中的内容复制到tempPix中，保证以前的内容不消失
            self.tempPix = self.pix
            pp = QPainter(self.tempPix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.tempPix)
        else:
            pp = QPainter(self.pix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.pix)
            
    #3
    def mousePressEvent(self, event):
        #按下鼠标左键
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
            self.isDrawing = True
    
    #4
    def mouseReleaseEvent(self, event):
        #释放鼠标左键
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            #进行重新绘制
            self.update()
            self.isDrawing = False
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
