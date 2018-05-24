import sys
from PyQt5.QtWidgets import QWidget,  QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem
from PyQt5.QtCore import Qt
class Table(QWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("QTableWidget例子")
        self.resize(400, 300)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget)
        
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
        tableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])
        #合并单元格
        tableWidget.setSpan(0, 0, 3, 1)
        newItem = QTableWidgetItem("张三")
        #设置对其方式右对齐与底部对齐
        newItem.setTextAlignment(Qt.AlignRight|Qt.AlignBottom)
        tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem("男")
        tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem("160")
        tableWidget.setItem(0, 2, newItem)
    
        self.setLayout(conLayout)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Table()
    demo.show()
    sys.exit(app.exec_())
