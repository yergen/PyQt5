from PyQt5.QtWidgets import QApplication,  QWidget,  QPushButton
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    btn = QPushButton(widget)
    btn.setText("Button")
    #以QWidget的左上角为(0, 0)点
    btn.move(20, 20)
    #不同操作系统可能对窗口的最小宽度有规定，若设置宽度小于规定值，则会以规定值进行显示
    widget.resize(300, 200)
    widget.move(250, 200)
    
    widget.setWindowTitle('PyQt坐标系统例子')
    widget.show()
    print("QWidget:")
    print("w.x()=%d " % widget.x())#窗口左上角坐标
    print("w.y()=%d " % widget.y())
    print("w.width()=%d " % widget.width())#客户区的宽
    print("w.height()=%d " % widget.height())
    
    print("QWidget.geometry:")
    print("w.geometry().x()=%d " % widget.geometry().x())#客户区左上角坐标
    print("w.geometry().y()=%d " % widget.geometry().y())
    print("w.geometry().width()=%d " % widget.geometry().width())#客户区的宽
    print("w.geometry().height()=%d " % widget.geometry().height())
    
    print("w.frameGeometry().width()=%d " % widget.frameGeometry().width())#包含边框的宽
    print("w.frameGeometry().height()=%d " % widget.frameGeometry().height())
    sys.exit(app.exec_())
