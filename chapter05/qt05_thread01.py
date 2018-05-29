import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

global sec
sec = 0

def setTime():
    global sec
    sec+=1
    #LED显示数字+1
    lcdNumber.display(sec)

def work():
    #计数器每秒计数
    timer.start(1000)
    for i in range(2000000000):
        pass
    
    timer.stop()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)
    
    #垂直布局类QVBoxLayout
    layout = QVBoxLayout(top)
    #添加一个显示面板
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("测试")
    layout.addWidget(button)
    
    timer = QTimer()
    timer.timeout.connect(setTime)
    button.clicked.connect(work)
    
    top.show()
    sys.exit(app.exec_())
    
    
