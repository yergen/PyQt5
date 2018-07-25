import time
import os

if __name__ == '__main__':
    #切换到openweb.py文件所在的工作目录。
    os.chdir('E:\pyqt5\chapter10\example3')
    for i in range(5):
        os.system("python openweb.py")
        print("正在刷新页面。次数=>", i)
        time.sleep(10)
