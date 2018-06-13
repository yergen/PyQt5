from PyQt5.QtWidgets import *
import sys

class WindowDemo(QWidget):
    def __init__(self, parent=None):
        super(WindowDemo, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        combo = QComboBox(self)
        combo.setObjectName('myQComboBox')
        combo.addItem('Window')
        combo.addItem('Ubuntu')
        combo.addItem('Red Hat')
        combo.move(50, 50)
        self.setGeometry(250, 200, 320, 150)
        self.setWindowTitle('QComboBox样式')
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    #定义QComboBox控件的QSS样式
    qssStyle = '''
                QComboBox#myQComboBox::drop-down{
                    image:url(./images/dropdown.png)
                }
    '''
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec_())
    
