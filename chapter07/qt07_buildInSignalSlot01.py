from PyQt5.QtWidgets import *
import sys

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("内置信号/槽示例")
        self.resize(330, 50)
        btn = QPushButton("关闭", self)
        btn.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
