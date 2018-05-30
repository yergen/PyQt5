from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys

class WindowDemo(QWidget):
    def __init__(self, parent=None):
        super(WindowDemo, self).__init__(parent)
        
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn1.setText("button 1")
        btn2.setText("button 2")
        btn3.setText("button 3")
        
        hbox = QHBoxLayout()
        
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        self.setLayout(hbox)
        
        #添加伸缩控件
        hbox.addStretch(0)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    demo = WindowDemo()
    demo.show()
    sys.exit(app.exec_())
