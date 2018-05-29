import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel("<font color=red size=128><b>Hello PyQt,窗口会在10秒后消失！</b></font>")
    #启动画面、无边框窗口
    label.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
    label.show()
    #设置10秒后自动退出
    QTimer.singleShot(10000, app.quit)
    sys.exit(app.exec_())
