# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pyqt5\chapter09\matplotlib_pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.matplotlibwidget_static = MatplotlibWidget(self.centralWidget)
        self.matplotlibwidget_static.setGeometry(QtCore.QRect(50, 20, 561, 271))
        self.matplotlibwidget_static.setObjectName("matplotlibwidget_static")
        self.matplotlibwidget_dynamic = MatplotlibWidget(self.centralWidget)
        self.matplotlibwidget_dynamic.setGeometry(QtCore.QRect(49, 289, 561, 271))
        self.matplotlibwidget_dynamic.setObjectName("matplotlibwidget_dynamic")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 440, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "显示静态图"))
        self.pushButton_2.setText(_translate("MainWindow", "显示动态图"))

from MatplotlibWidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

