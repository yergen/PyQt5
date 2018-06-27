import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase
class ExecDatabaseDemo(QWidget):
    def __init__(self, parent=None):
        super(ExecDatabaseDemo, self).__init__(parent)
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./db/database.db')
        #打开数据库
        self.db.open()
    
    def closeEvent(self, event):
        #关闭数据库
        self.db.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ExecDatabaseDemo()
    demo.show()
    sys.exit(app.exec_())
    
