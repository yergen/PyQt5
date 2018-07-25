# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pyqt5\chapter11\fundFOF.ui'
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 580))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_parameter_tree = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_parameter_tree.setMinimumSize(QtCore.QSize(100, 0))
        self.widget_parameter_tree.setObjectName("widget_parameter_tree")
        self.horizontalLayout.addWidget(self.widget_parameter_tree)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.QWebEngineView_ProductVsHs300 = QtWebEngineWidgets.QWebEngineView(self.scrollAreaWidgetContents)
        self.QWebEngineView_ProductVsHs300.setMinimumSize(QtCore.QSize(0, 100))
        self.QWebEngineView_ProductVsHs300.setStyleSheet("background-color: rgb(167, 167, 167);")
        self.QWebEngineView_ProductVsHs300.setObjectName("QWebEngineView_ProductVsHs300")
        self.verticalLayout_2.addWidget(self.QWebEngineView_ProductVsHs300)
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.QWebEngineView_MonthReturn = QtWebEngineWidgets.QWebEngineView(self.tab)
        self.QWebEngineView_MonthReturn.setStyleSheet("background-color: rgb(167, 167, 167);")
        self.QWebEngineView_MonthReturn.setObjectName("QWebEngineView_MonthReturn")
        self.horizontalLayout_5.addWidget(self.QWebEngineView_MonthReturn)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QWebEngineView_WeekReturn = QtWebEngineWidgets.QWebEngineView(self.tab_2)
        self.QWebEngineView_WeekReturn.setStyleSheet("background-color: rgb(167, 167, 167);")
        self.QWebEngineView_WeekReturn.setObjectName("QWebEngineView_WeekReturn")
        self.verticalLayout.addWidget(self.QWebEngineView_WeekReturn)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.QWebEngineView_LagestBack = QtWebEngineWidgets.QWebEngineView(self.tab_3)
        self.QWebEngineView_LagestBack.setStyleSheet("background-color: rgb(167, 167, 167);")
        self.QWebEngineView_LagestBack.setObjectName("QWebEngineView_LagestBack")
        self.horizontalLayout_3.addWidget(self.QWebEngineView_LagestBack)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "月度收益"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "区间收益"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "回撤情况"))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

