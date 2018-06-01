import sys
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt

class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle("信号与槽：连接滑块LCD")
        #先创建滑块和LCD控件
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        
        vBox = QVBoxLayout()
        vBox.addWidget(lcd)
        vBox.addWidget(slider)
        
        self.setLayout(vBox)
        slider.valueChanged.connect(lcd.display)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
        
