import sys
from PyQt5.QtWidgets import QWidget,  QTableWidget, QHBoxLayout, \
QApplication, QTableWidgetItem, QAbstractItemView, QComboBox, QPushButton

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
        newItem = QTableWidgetItem("张三")
        tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem("男")
        tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem("160")
        tableWidget.setItem(0, 2, newItem)
#        comBox = QComboBox();
#        comBox.addItem("男")
#        comBox.addItem("女")
#        comBox.setStyleSheet("QComboBox{margin:3px};")
#        tableWidget.setCellWidget(0, 1, comBox)
#        
#        searchBtn = QPushButton("修改")
#        searchBtn.setDown(True)
#        searchBtn.setStyleSheet("QPushButton{margin:3px};")
#        tableWidget.setCellWidget(0, 2, searchBtn)
        
#        #将表格变为禁止编辑
#        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
#        #设置表格整行选中
#        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
#        #将行和列的宽度、高度设置为所显示内容的宽度、高度相匹配
#        tableWidget.resizeColumnsToContents()
#        tableWidget.resizeRowsToContents()
#        #表格头的显示与隐藏
#        tableWidget.verticalHeader().setVisible(False)
#        tableWidget.horizontalHeader().setVisible(False)
    
    
        self.setLayout(conLayout)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Table()
    demo.show()
    sys.exit(app.exec_())
    
        
