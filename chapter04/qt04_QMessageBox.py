import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("QMessageBox例子")
        self.resize(300, 100)
        self.myButton = QPushButton(self)
        self.myButton.setText("点击弹出消息框")
        self.myButton.clicked.connect(self.msg)
    
    def msg(self):
        #使用information消息框
        reply = QMessageBox.information(self, "标题","消息正文", \
                   QMessageBox.Yes | QMessageBox.No,  QMessageBox.Yes)
        print(reply)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
