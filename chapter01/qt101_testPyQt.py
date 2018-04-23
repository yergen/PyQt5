# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:55:40 2018

@author: Administrator
"""

import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("hello, pyqt5")
widget.show()
sys.exit(app.exec_())