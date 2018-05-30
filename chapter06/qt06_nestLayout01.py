import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,\
                QVBoxLayout, QGridLayout, QFormLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle('嵌套布局示例')
        
        #全局布局（1种）:水平
        wlayout = QHBoxLayout()
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
        
        #准备四个控件
        hwg = QWidget()
        vwg = QWidget()
        gwg = QWidget()
        fwg = QWidget()
        
        #使用四个控件设置局部布局
        hwg.setLayout(hlayout)
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(formlayout)
        
        #将四个控件添加到全局布局中
        wlayout.addWidget(hwg)
        wlayout.addWidget(vwg)
        wlayout.addWidget(gwg)
        wlayout.addWidget(fwg)
        
        #将窗口本身设置为全局布局
        self.setLayout(wlayout)

if __name__=='__main__':
    app = QApplication(sys.argv)
    demo = MyWindow()
    demo.show()
    sys.exit(app.exec_())
