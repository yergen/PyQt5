from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    #设置窗口名
    win.setObjectName("MainWindow")
    #设置图片的相对路径
    win.setStyleSheet("#MainWindow{border-image:url(images/python.jpg);}")
    #设置窗口的背景色
#    win.setStyleSheet("#MainWindow{background-color:yellow}")
    win.show()
    sys.exit(app.exec_())
