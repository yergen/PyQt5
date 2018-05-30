import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,\
                QVBoxLayout, QGridLayout, QFormLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle('嵌套布局示例')
        self.resize(500, 150)
        #全局控件(注意参数self)，用于”承载“全局布局
        wwg = QWidget(self)
        
        #全局布局（注意参数wwg）
        wl = QHBoxLayout(wwg)
        #局部布局（4种）:水平、垂直、网格、表单
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        glayout = QGridLayout()
        formlayout = QFormLayout()
        
        #为局部布局添加控件
        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))
        vlayout.addWidget(QPushButton(str(3)))
        vlayout.addWidget(QPushButton(str(4)))
        glayout.addWidget(QPushButton(str(5)), 0, 0)
        glayout.addWidget(QPushButton(str(6)), 0, 1)
        glayout.addWidget(QPushButton(str(7)), 1, 0)
        glayout.addWidget(QPushButton(str(8)), 1, 1)
        formlayout.addWidget(QPushButton(str(9)))
        formlayout.addWidget(QPushButton(str(10)))
        formlayout.addWidget(QPushButton(str(11)))
        formlayout.addWidget(QPushButton(str(12)))
        
        #这里在局部布局中添加控件，然后将其添加到全局布局中
        wl.addLayout(hlayout)
        wl.addLayout(vlayout)
        wl.addLayout(glayout)
        wl.addLayout(formlayout)
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    demo = MyWindow()
    demo.show()
    sys.exit(app.exec_())
