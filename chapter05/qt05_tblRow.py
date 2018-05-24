import sys
from PyQt5.QtWidgets import QWidget,  QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem

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
        #在表格中不显示分割线
        tableWidget.setShowGrid(False)
        
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
        tableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])
        #将第一列单元格宽度设置为150
        tableWidget.setColumnWidth(0, 150)
        #将第一行单元格高度设置为120
        tableWidget.setRowHeight(0, 120)
        newItem = QTableWidgetItem("张三")
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
