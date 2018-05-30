import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("垂直布局管理例子")
        
        #水平布局从左到右的顺序添加按钮控件
        vlayout = QVBoxLayout()
        vlayout.addWidget(QPushButton(str(1)))
        vlayout.addWidget(QPushButton(str(2)))
        vlayout.addWidget(QPushButton(str(3)))
        vlayout.addWidget(QPushButton(str(4)))
        vlayout.addWidget(QPushButton(str(5)))
        self.setLayout(vlayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
