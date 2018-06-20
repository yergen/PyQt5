import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QCursor
from PyQt5.QtCore import Qt

class ShapeWidget(QWidget):
    def __init__(self, parent=None):
        super(ShapeWidget, self).__init__(parent)
        self.setWindowTitle("不规则的可以拖动的窗口实现例子")
        self.mypix()
    
    #显示不规则的图片
    def mypix(self):
        self.update()
        self.mypic = './images/boy.png'
        self.pix = QPixmap(self.mypic, "0", Qt.AvoidDither | Qt.ThresholdDither | Qt.ThresholdAlphaDither)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.dragPosition = None
    
    #重新定义鼠标按下响应函数mousePressEvent和鼠标指针移动响应函数mouseMoveEvent，
    #使不规则窗口能响应鼠标事件，随意拖动窗口
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            #当使用左键移动窗口时修改偏移值
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    #在窗口中首次绘制时，会加载paintEvent()函数
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
        
    #鼠标双击事件
    def mouseDoubleClickEvent(self, event):
        self.mypix()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ShapeWidget()
    form.show()
    sys.exit(app.exec_())
            
    
