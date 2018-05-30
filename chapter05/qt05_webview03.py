from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(122, 30, 1355, 730)
        self.browser = QWebEngineView()
        #加载外部的Web页面
        self.browser.setHtml('''
        <!DocTYPE html>
        <html>
            <head>
            <meta charset="UTF-8">
            <title></title>
            </head>
            <body>
                <h1>Hello PyQt5<h1>
                <h1>Hello PyQt5<h1>
                <h1>Hello PyQt5<h1>
                <h1>Hello PyQt5<h1>
            </body>
        </html>
        '''
        )
        self.setCentralWidget(self.browser)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
        
