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
        #设置伸缩量为1
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        #设置伸缩量为1
        hbox.addStretch(1)
        hbox.addWidget(btn2)
        #设置伸缩量为1
        hbox.addStretch(1)
        hbox.addWidget(btn3)
        #设置伸缩量为1
        hbox.addStretch(1)
        self.setLayout(hbox)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    demo = WindowDemo()
    demo.show()
    sys.exit(app.exec_())
