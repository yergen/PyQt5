import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("水平布局管理例子")
        
        #水平布局从左到右的顺序添加按钮控件
        hlayout = QHBoxLayout()
        #水平居左、垂直靠上对齐
        hlayout.addWidget(QPushButton(str(1)), 0, Qt.AlignLeft|Qt.AlignTop)
        hlayout.addWidget(QPushButton(str(2)), 0, Qt.AlignLeft|Qt.AlignTop)
        hlayout.addWidget(QPushButton(str(3)))
        hlayout.addWidget(QPushButton(str(4)), 0, Qt.AlignRight|Qt.AlignBottom)
        hlayout.addWidget(QPushButton(str(5)), 0, Qt.AlignRight|Qt.AlignBottom)
        self.setLayout(hlayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
