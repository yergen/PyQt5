import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate

class CalendarExample(QWidget):
    def __init__(self, parent=None):
        super(CalendarExample, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1980, 1, 1))
        self.cal.setMaximumDate(QDate(3000, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)
        self.lb1 = QLabel(self)
        date = self.cal.selectedDate()
        self.lb1.setText(date.toString("yyyy-MM-dd dddd"))
        self.lb1.move(20, 300)
        self.setGeometry(100, 100, 400, 350)
        self.setWindowTitle("Calendar 例子")
    
    def showDate(self, date):
        self.lb1.setText(date.toString("yyyy-MM-dd dddd"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = CalendarExample()
    demo.show()
    sys.exit(app.exec_())
