import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        #调用父类构造函数
        super(MyWindow, self).__init__(parent)
        
        #设置窗口标志（无边框）
        self.setWindowFlags(Qt.FramelessWindowHint)
        #为了便于显示，设置窗口背景颜色（采用QSS）
        self.setStyleSheet('''background-color:blue;''')
    
    def showMaximized(self):
        #最大化窗口
        #得到桌面控件
        desktop = QApplication.desktop()
        #得到屏幕可显示尺寸
        rect = desktop.availableGeometry()
        #设置窗口尺寸
        self.setGeometry(rect)
        #显示窗口
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.showMaximized()
    sys.exit(app.exec_())
