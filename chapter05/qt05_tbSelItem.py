import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QBrush

class Table(QWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(600, 800)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(30)
        tableWidget.setColumnCount(4)
        conLayout.addWidget(tableWidget)
        
        for i in range(30):
            for j in range(4):  
                itemContent = '(%d,%d)'% (i, j)
                tableWidget.setItem(i, j, QTableWidgetItem(itemContent))
        self.setLayout(conLayout)
        
        #遍历表格查找对应项
        text = "(10,1)"
        items = tableWidget.findItems(text, QtCore.Qt.MatchExactly)
        item = items[0]
        #选中单元格
        item.setSelected(True)
        #设置单元格的背景颜色为红色
        item.setForeground(QBrush(QColor(255, 0, 0)))
        
        row = item.row()
        #通过鼠标滚轮定位，快速定位到第11行
        tableWidget.verticalScrollBar().setSliderPosition(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
        
