from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import sys

class ListViewDemo(QWidget):
    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView 例子")
        self.resize(300, 270)
        layout = QVBoxLayout()
        
        listView = QListView()
        slm = QStringListModel()
        self.qList = ['Item1', 'Item2', 'Item3', 'Item4']
        slm.setStringList(self.qList)
        listView.setModel(slm)
        listView.clicked.connect(self.clicked)
        layout.addWidget(listView)
        self.setLayout(layout)
        
    def clicked(self, qModelIndex):
        QMessageBox.information(self, "ListWidget", "你选择了：" +self.qList[qModelIndex.row()])
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ListViewDemo()
    demo.show()
    sys.exit(app.exec_())
        
