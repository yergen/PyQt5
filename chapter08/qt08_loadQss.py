import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from CommonHelper import CommonHelper
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.resize(477, 258) 
    win.setWindowTitle("加载QSS文件")
    
    btn1 = QPushButton(win)
    btn1.setText("添加")
    btn1.setToolTip("测试提示")
    styleFile = './style.qss'
    #换肤时进行全局修改，只需修改不同的QSS文件即可
    style = CommonHelper.readQss(styleFile)
    win.setStyleSheet(style)
    win.show()
    sys.exit(app.exec_())
