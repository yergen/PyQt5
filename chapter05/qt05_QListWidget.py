import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ListWidgetDemo(QListWidget):
    def __init__(self, parent=None):
        super(ListWidgetDemo, self).__init__(parent)
        self.resize(300, 120)
        self.setWindowTitle("QListwidget例子")
        
        for index in range(1, 5):
            self.addItem("Item %s" %index)
        
        self.itemClicked.connect(self.clicked)
        
    def clicked(self, item):
        QMessageBox.information(self, "ListWidget", "你选择了："+item.text())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ListWidgetDemo()
    demo.show()
    sys.exit(app.exec_())
        
