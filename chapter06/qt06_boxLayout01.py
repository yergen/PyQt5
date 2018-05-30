import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("水平布局管理例子")
        
        #水平布局从左到右的顺序添加按钮控件
        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))
        hlayout.addWidget(QPushButton(str(3)))
        hlayout.addWidget(QPushButton(str(4)))
        hlayout.addWidget(QPushButton(str(5)))
        #设置控件间距
        hlayout.setSpacing(0)
        self.setLayout(hlayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
