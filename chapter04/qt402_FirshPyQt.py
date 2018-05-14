#-*- coding: UTF-8 -*-
import sys 
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300, 200)
    window.move(250, 150)
    window.setWindowTitle('Hello PyQt5')
    window.show()
    sys.exit(app.exec_())
    
    
