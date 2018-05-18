import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ToolBardemo(QMainWindow):
    def __init__(self, parent=None):
        super(ToolBardemo, self).__init__(parent)
        self.setWindowTitle("toolbar例子")
        self.resize(300, 200)
        layout = QVBoxLayout()
        tb = self.addToolBar("File")
        new = QAction(QIcon("./images/new.png"), "new", self)
        tb.addAction(new)
        open = QAction(QIcon("./images/open.png"), "open", self)
        tb.addAction(open)
        save = QAction(QIcon("./images/save.png"), "save", self)
        tb.addAction(save)
        tb.actionTriggered[QAction].connect(self.tooltbnpressed)
        self.setLayout(layout)
    
    def tooltbnpressed(self, a):
        print("pressed tool button is", a.text())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ToolBardemo()
    demo.show()
    sys.exit(app.exec_())
