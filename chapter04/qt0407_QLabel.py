from PyQt5.QtWidgets import *
import sys

class QlabelDemo(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('QLabel例子')
        nameLb1 = QLabel('&Name', self)
        nameEb1 = QLineEdit(self)
        nameLb1.setBuddy(nameEb1)
        
        nameLb2 = QLabel('&Password', self)
        nameEb2 = QLineEdit(self)
        nameLb2.setBuddy(nameEb2)
        
        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLb1, 0, 0)
        mainLayout.addWidget(nameEb1, 0, 1, 1, 2)
        
        mainLayout.addWidget(nameLb2, 1, 0)
        mainLayout.addWidget(nameEb2, 1, 1, 1, 2)
        
        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    labelDemo = QlabelDemo()
    labelDemo.show()
    sys.exit(app.exec_())
    
    
        
