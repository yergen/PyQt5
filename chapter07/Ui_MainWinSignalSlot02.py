# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pyqt5\chapter07\MainWinSignalSlot02.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 372)
        self.controlsGroup = QtWidgets.QGroupBox(Form)
        self.controlsGroup.setGeometry(QtCore.QRect(40, 30, 401, 161))
        self.controlsGroup.setObjectName("controlsGroup")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.controlsGroup)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 330, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numberSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.horizontalLayout.addWidget(self.numberSpinBox)
        self.styleCombo = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.styleCombo.setObjectName("styleCombo")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.horizontalLayout.addWidget(self.styleCombo)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.printButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.printButton.setObjectName("printButton")
        self.horizontalLayout.addWidget(self.printButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.controlsGroup)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 110, 160, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewStatus = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.previewStatus.setObjectName("previewStatus")
        self.horizontalLayout_2.addWidget(self.previewStatus)
        self.previewButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout_2.addWidget(self.previewButton)
        self.resultGroup = QtWidgets.QGroupBox(Form)
        self.resultGroup.setGeometry(QtCore.QRect(450, 30, 261, 161))
        self.resultGroup.setObjectName("resultGroup")
        self.resultLabel = QtWidgets.QLabel(self.resultGroup)
        self.resultLabel.setGeometry(QtCore.QRect(0, 10, 261, 151))
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.controlsGroup.setTitle(_translate("Form", "打印控制"))
        self.label.setText(_translate("Form", "打印份数："))
        self.styleCombo.setCurrentText(_translate("Form", "A4"))
        self.styleCombo.setItemText(0, _translate("Form", "A4"))
        self.styleCombo.setItemText(1, _translate("Form", "A3"))
        self.styleCombo.setItemText(2, _translate("Form", "A5"))
        self.label_2.setText(_translate("Form", "纸张类型："))
        self.printButton.setText(_translate("Form", "打印"))
        self.previewStatus.setText(_translate("Form", "全屏预览"))
        self.previewButton.setText(_translate("Form", "预览"))
        self.resultGroup.setTitle(_translate("Form", "操作控制"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

