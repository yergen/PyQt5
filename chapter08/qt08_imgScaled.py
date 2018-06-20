import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ImgScaled(QWidget):
    def __init__(self, parent=None):
        super(ImgScaled, self).__init__(parent)
        self.setWindowTitle("图片大小缩放例子")
        #filename 为图片的路径
        filename = r"./images/Cloudy_72px.png"
        img = QImage(filename)
        #设置标签的宽度为120像素，高度为120像素，所加载的图片按照标签的高度和宽度等比例缩放
        label1 = QLabel(self)
        label1.setFixedWidth(120)
        label1.setFixedHeight(120)
        #缩放图片，以固定大小显示
        result = img.scaled(label1.width(), label1.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        #在标签控件上显示图片
        label1.setPixmap(QPixmap.fromImage(result))
        
        vbox = QVBoxLayout(self)
        vbox.addWidget(label1)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ImgScaled()
    demo.show()
    sys.exit(app.exec_())
