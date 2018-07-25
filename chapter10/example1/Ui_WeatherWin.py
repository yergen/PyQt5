# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pyqt5\chapter10\example1\WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(436, 341)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 411, 231))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 22, 54, 20))
        self.label.setObjectName("label")
        self.weatherComboBox = QtWidgets.QComboBox(self.groupBox)
        self.weatherComboBox.setGeometry(QtCore.QRect(80, 20, 251, 22))
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(20, 50, 371, 171))
        self.resultText.setObjectName("resultText")
        self.queryBtn = QtWidgets.QPushButton(Form)
        self.queryBtn.setGeometry(QtCore.QRect(80, 280, 75, 23))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(210, 280, 75, 23))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Form)
        self.queryBtn.clicked.connect(Form.queryWeather)
        self.clearBtn.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "查询天气"))
        self.label.setText(_translate("Form", "城市"))
        self.weatherComboBox.setItemText(0, _translate("Form", "北京"))
        self.weatherComboBox.setItemText(1, _translate("Form", "天津"))
        self.weatherComboBox.setItemText(2, _translate("Form", "上海"))
        self.queryBtn.setText(_translate("Form", "查询"))
        self.clearBtn.setText(_translate("Form", "清空"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

