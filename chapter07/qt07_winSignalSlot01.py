from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QMessageBox
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    
    def showMsg():
        QMessageBox.information(widget, "信息提示框", "ok,弹出测试信息")
        
    btn = QPushButton("测试点击按钮", widget)
    btn.clicked.connect(showMsg)
    widget.show()
    sys.exit(app.exec_())
