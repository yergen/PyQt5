# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pyqt5\chapter09\pyqtgraph_pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pyqtgraph1 = GraphicsLayoutWidget(self.centralWidget)
        self.pyqtgraph1.setGeometry(QtCore.QRect(20, 10, 541, 221))
        self.pyqtgraph1.setObjectName("pyqtgraph1")
        self.pyqtgraph2 = GraphicsLayoutWidget(self.centralWidget)
        self.pyqtgraph2.setGeometry(QtCore.QRect(20, 240, 311, 341))
        self.pyqtgraph2.setObjectName("pyqtgraph2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 380, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "水平绘图"))
        self.pushButton_2.setText(_translate("MainWindow", "垂直绘图"))

from pyqtgraph import GraphicsLayoutWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

