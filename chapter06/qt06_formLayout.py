from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit
import sys

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle('表单布局管理例子')
        self.resize(400, 100)
        
        formlayout = QFormLayout()
        labl1 = QLabel('标签1')
        lineEdit1 = QLineEdit()
        labl2 = QLabel('标签2')
        lineEdit2 = QLineEdit()
        labl3 = QLabel('标签3')
        lineEdit3 = QLineEdit()
        
        formlayout.addRow(labl1, lineEdit1)
        formlayout.addRow(labl2, lineEdit2)
        formlayout.addRow(labl3, lineEdit3)
        
        self.setLayout(formlayout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
    
