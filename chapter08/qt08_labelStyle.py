import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class LabelStyle(QWidget):
    def __init__(self, parent=None):
        super(LabelStyle, self).__init__(parent)
        self.setWindowTitle("按钮和Label背景图片例子")
        #为标签添加背景图片
        label1 = QLabel(self)
        label1.setToolTip('这是一个文本标签')
        label1.setStyleSheet("QLabel{border-image:url(./images/python.jpg);}")
        #设置标签的宽度和高度
        label1.setFixedWidth(476)
        label1.setFixedHeight(259)
        
        #为按钮添加背景图片
        btn1 = QPushButton(self)
        btn1.setObjectName('btn1')
        btn1.setMaximumSize(64, 64)
        btn1.setMinimumSize(64, 64)
        style = '''
            #btn1{
            
                border-radius: 30px;
                background-image: url('./images/left.png');
            }
            
            #btn1:hover{
                border-radius: 30px;
                background-image: url('./images/leftHover.png');
            }
            
             #btn1:Pressed{
                border-radius: 30px;
                background-image: url('./images/leftPressed.png');
            }
        '''
        btn1.setStyleSheet(style)
        
        #布局
        vbox = QVBoxLayout(self)
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(btn1)
        
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = LabelStyle()
    demo.show()
    sys.exit(app.exec_())
