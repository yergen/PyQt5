import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        #1
        grid = QGridLayout()
        self.setLayout(grid)
        
        #2
        names = ['Cls', 'Bck', '', 'Close', 
                    '7', '8', '9', '/',
                    '4', '5', '6', '*',
                    '1', '2', '3', '-',
                    '0', '.', '=', '+']
        #3
        positions =[(i, j) for i in range(5) for j in range(4)]
       
        # 4
        for position,  name in zip(positions, names):
            if name =='':
                continue
                
            button = QPushButton(name)
            grid.addWidget(button, *position)
        
        self.move(300, 150)
        self.setWindowTitle('网络布局管理例子')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = WinForm()
    demo.show()
    sys.exit(app.exec_())
            
