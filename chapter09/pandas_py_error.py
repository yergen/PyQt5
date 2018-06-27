#-*- coding: utf-8 -*-

'''
Module implementing MainWindow
'''

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

import pandas as pd
from qtpandas.models.DataFrameModel import DataFrameModel

from Ui_pandas_pyqt import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        widget = self.pandastablewidget
        widget.resize(600, 500)
        self.model = DataFrameModel()#设置新的模型
        widget.setViewModel(self.model)
        self.df = pd.read_excel(r'./data/fund_data.xlsx', encoding='gdk')
        self.df_original = self.df.copy()#备份原始数据
        self.model.setDataFrame(self.df)
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.model.setDataFrame(self.df_original)
    
    @pyqtSlot()
    def on_pushButton2_clicked(self):
        self.df.to_excel(r'./data/fund_data_new.xlsx')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
        
