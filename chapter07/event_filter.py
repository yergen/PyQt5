#-*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class EventFilter(QDialog):
    def __init__(self, parent=None):
        super(EventFilter, self).__init__(parent)
        self.setWindowTitle("事件过滤器")
        
        self.label1 = QLabel("请点击")
        self.label2 = QLabel("请点击")
        self.label3 = QLabel("请点击")
        self.LabelState = QLabel("test")
        
        self.image1 = QImage("images/cartoon1.ico")
        self.image2 = QImage("images/cartoon2.ico")
        self.image3 = QImage("images/cartoon3.ico")
        
        self.width = 600
        self.height = 300
        
        self.resize(self.width, self.height)
        #对过滤的控件设置installEventFilter
        self.label1.installEventFilter(self)
        self.label2.installEventFilter(self)
        self.label3.installEventFilter(self)
        
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(self.label1, 5, 0)
        mainLayout.addWidget(self.label2, 5, 1)
        mainLayout.addWidget(self.label3, 5, 2)
        mainLayout.addWidget(self.LabelState, 6, 1)
        self.setLayout(mainLayout)
    
    def eventFilter(self, watched, event):
        #只对label1的点击事件进行过滤，重写其行为，其他事件会被忽略
        if watched == self.label1:
            #这里对鼠标按下事件进行过滤，重写其行为
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.LabelState.setText("按下鼠标左键")
                elif mouseEvent.buttons() == Qt.MidButton:
                    self.LabelState.setText("按下鼠标中键")
                elif mouseEvent.buttons() == Qt.RightButton:
                    self.LabelState.setText("按下鼠标右键")
                
                #转换图片大小
                transform = QTransform()
                transform.scale(0.5, 0.5)
                tmp = self.image1.transformed(transform)
                self.label1.setPixmap(QPixmap.fromImage(tmp))
            #这里对鼠标释放事件进行过滤，重写其行为
            if event.type() == QEvent.MouseButtonRelease:
                self.LabelState.setText("释放鼠标按键")
                self.label1.setPixmap(QPixmap.fromImage(self.image1))
        #对于其他情况，会返回系统默认的事件处理方法
        return QDialog.eventFilter(self, watched, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = EventFilter()
    #在QApplication中安装事件过滤器
#    app.installEventFilter(dialog)
    dialog.show()
    sys.exit(app.exec_())
