import sys
from PyQt5.QtWidgets import QWidget,  QTableWidget, QHBoxLayout, \
QApplication, QTableWidgetItem, QAbstractItemView, QComboBox, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

class Table(QWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(500, 500)
        conLayout = QHBoxLayout()
        table = QTableWidget()
        table.setColumnCount(3)
        table.setRowCount(5)
        
        table.setHorizontalHeaderLabels(['图片1', '图片2', '图片3'])
        
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setIconSize(QSize(300, 200))
        
        for i in range(3):      #让列宽和图片相同
            table.setColumnWidth(i, 150)
        for i in range(5):      #让行高和图片相同
            table.setRowHeight(i, 150)
        
        for k in range(15):    #模拟产生15条记录
            i = k/3
            j = k%3
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled) #用户点击表格时，图片被选中
            icon = QIcon(r'./images/bao%d.png' %k)
            item.setIcon(QIcon(icon))
            
            print('e/icons/%d.png i=%d j=%d' %(k, i, j))
            table.setItem(i, j , item)
            
        conLayout.addWidget(table)
        self.setLayout(conLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Table()
    demo.show()
    sys.exit(app.exec_())



