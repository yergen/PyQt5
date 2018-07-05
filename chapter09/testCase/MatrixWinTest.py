import unittest
import time
import sys
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QThread,pyqtSignal
import CallMatrixWinUi

class MatrixWinTest(unittest.TestCase):
    #初始化工作
    def setUp(self):
        print('***setUp***')
        self.app = QApplication(sys.argv)
        self.form = CallMatrixWinUi.CallMatrixWinUi()
        self.form.show()
        
        #新建线程对象，传入参数，每5秒关闭一个测试用例
        self.bkThread = BackWorkThread(int(2))
        #连接子进程的信号和槽
        self.bkThread.finishSignal.connect(self.closeWindow)
#        self.bkThread.finishSignal.connect(self.app.exec_)
        #启动线程，开始执行run()函数中的内容
        self.bkThread.start()
        
    #退出清理工作
    def tearDown(self):
        print('***tearDown***')
        self.app.exec_()
    #关闭窗口
    def closeWindow(self):
        print('关闭窗口...')
        self.app.quit()
    #设置窗口中所有控件的值为0，状态设置为初始状态
    def setFormToZero(self):
        print('* setFormToZero *')
        self.form.ui.tequilaScrollBar.setValue(0)
        self.form.ui.tripleSecSpinBox.setValue(0)
        self.form.ui.limeJuiceLineEdit.setText("0.0")
        self.form.ui.iceHorizontalSlider.setValue(0)
        
        self.form.ui.selScrollBarLbl.setText("0")
        self.form.ui.selIceSliderLbl.setText("0")
    #测试用例-在默认状态下测试GUI
    def test_defaults(self):
        #测试GUI处于默认状态
        print('***testCase test_defaults begin***')
        self.form.setWindowTitle('开始测试用例test_defaults')
        
        self.assertEqual(self.form.ui.tequilaScrollBar.value(), 8)
        self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 4)
        self.assertEqual(self.form.ui.limeJuiceLineEdit.text(), "12.0")
        self.assertEqual(self.form.ui.iceHorizontalSlider.value(), 12)
        self.assertEqual(self.form.ui.speedButtonGroup.checkedButton().text(), "&Karate Chop")
        print('***speedName' + self.form.getSpeedName())
        
        #用鼠标左键单击"OK"按钮
        okWidget = self.form.ui.okBtn
        QTest.mouseClick(okWidget, Qt.LeftButton)
        
        #测试窗口在默认状态下，各控件的默认自是否与预期值一样
        self.assertEqual(self.form.getJiggers(), 36.0)
        self.assertEqual(self.form.getSpeedName(), "&Karate Chop")
        print('***testCase test_defaults end***')
    #测试用例-测试滑动条
    def test_moveScrollBar(self):
        #测试用例test_moveScrollBar
        print('***testCase test_moveScrollBar begin***')
        self.form.setWindowTitle('开始测试用例test_moveScrollBar')
        self.setFormToZero()
        
        #测试将龙舌兰酒的滑动条的值设置为12，在UI中实际它的最大值为11
        self.form.ui.tequilaScrollBar.setValue(12)
        print('*当执行self.form.ui.tequilaScrollBar.setValue(12)后, \
        ui.tequilaScrollBar.value() =>' + str(self.form.ui.tequilaScrollBar.value()))
        self.assertEqual(self.form.ui.tequilaScrollBar.value(), 11)
        
         #测试将龙舌兰酒的滑动条的值设置为-1，在UI中实际它的最大值为0
        self.form.ui.tequilaScrollBar.setValue(-1)
        print('*当执行self.form.ui.tequilaScrollBar.setValue(-1)后, \
        ui.tequilaScrollBar.value() =>' + str(self.form.ui.tequilaScrollBar.value()))
        self.assertEqual(self.form.ui.tequilaScrollBar.value(), 0)
        
        #重新将龙舌兰酒的滑动条的值设置为5
        self.form.ui.tequilaScrollBar.setValue(5)
        
        #用鼠标左键点击"OK"按钮
        okWidget = self.form.ui.okBtn
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.getJiggers(), 5)
        print('***testCase test_moveScrollBar end')
    #测试PyQt的QSpinBox
    def test_tripleSecSpinBox(self):
        #测试用例test_tripleSecSpinBox
        print('***testCase test_tripleSecSpinBox begin***')
        self.form.setWindowTitle('开始测试用例test_tripleSecSpinBox')
        self.setFormToZero()
        
        #测试将tripleSecSpinBox的值设置为12，在UI中实际它的最大值为11
        self.form.ui.tripleSecSpinBox.setValue(12)
        print('*当执行self.form.ui.tripleSecSpinBox.setValue(12)后, \
        ui.tripleSecSpinBox.value() =>' + str(self.form.ui.tripleSecSpinBox.value()))
        self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 11)
        
         #测试将test_tripleSecSpinBox的滑动条的值设置为-1，在UI中实际它的最大值为0
        self.form.ui.tripleSecSpinBox.setValue(-1)
        print('*当执行self.form.ui.tripleSecSpinBox.setValue(-1)后, \
        ui.tripleSecSpinBox.value() =>' + str(self.form.ui.tripleSecSpinBox.value()))
        self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 0)
        
        #重新将test_tripleSecSpinBox的滑动条的值设置为2
        self.form.ui.tripleSecSpinBox.setValue(2)
        
        #用鼠标左键点击"OK"按钮
        okWidget = self.form.ui.okBtn
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.getJiggers(), 2)
        print('***testCase test_tripleSecSpinBox end')
    
    #测试用例-测试柠檬汁单行文本框
    def test_limeJuiceLineEdit(self):
        #测试用例test_limeJuiceLineEdit
        print('***testCase test_limeJuiceLineEdit begin***')
        self.form.setWindowTitle('开始测试用例 test_limeJuiceLineEdit')
        self.setFormToZero()
        
        #清除lineEdit文本框控件值，然后在lineEdit文本框中输入"3.5"
        self.form.ui.limeJuiceLineEdit.clear()
#        QTest.keyClicks(self.form.ui.limeJuiceLineEdit, '3.5')
        self.form.ui.limeJuiceLineEdit.setText('3.5')
        
         #用鼠标左键点击"OK"按钮
        okWidget = self.form.ui.okBtn
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.getJiggers(), 3.5)
        print('***testCase test_limeJuiceLineEdit end')
    
    #测试用例-测试 iceHorizontalSlider
    def test_iceHorizontalSlider(self):
        #测试用例 test_iceHorizontalSlider
        print('***testCase test_iceHorizontalSlider begin***')
        self.form.setWindowTitle('开始测试用例 test_iceHorizontalSlider')
        self.setFormToZero()
    
        self.form.ui.iceHorizontalSlider.setValue(4)
        
        #用鼠标左键点击"OK"按钮
        okWidget = self.form.ui.okBtn
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.getJiggers(), 4)
        print('***testCase test_iceHorizontalSlider end')
    
    #测试用例-测试搅拌速度单选按钮
    def test_blenderSpeedButtons(self):
        #测试用例 test_blenderSpeedButtons
        print('***testCase test_blenderSpeedButtons begin***')
        self.form.ui.speedButton_1.click()
        self.assertEqual(self.form.getSpeedName(), "&Mix")
        self.form.ui.speedButton_2.click()
        self.assertEqual(self.form.getSpeedName(), "&Whip")
        self.form.ui.speedButton_3.click()
        self.assertEqual(self.form.getSpeedName(), "&Puree")
        self.form.ui.speedButton_4.click()
        self.assertEqual(self.form.getSpeedName(), "&Chop")
        self.form.ui.speedButton_5.click()
        self.assertEqual(self.form.getSpeedName(), "&Karate Chop")
        self.form.ui.speedButton_6.click()
        self.assertEqual(self.form.getSpeedName(), "&Beat")
        self.form.ui.speedButton_7.click()
        self.assertEqual(self.form.getSpeedName(), "&Smash")
        self.form.ui.speedButton_8.click()
        self.assertEqual(self.form.getSpeedName(), "&Liquefy")
        self.form.ui.speedButton_9.click()
        self.assertEqual(self.form.getSpeedName(), "&Vaporize")
        print('***testCase test_iceHorizontalSlider end')
    # 测试用例- 
    def test_liters(self):
        '''测试用例 test_liters '''		
        print('*** testCase test_liters begin ***')		
        self.form.setWindowTitle('开始测试用例 test_liters ')	
        
        self.setFormToZero()
        self.assertAlmostEqual(self.form.getLiters() , 0.0)
        self.form.ui.iceHorizontalSlider.setValue(1 )
        self.assertAlmostEqual(self.form.getLiters(), 0.0444)
        self.form.ui.iceHorizontalSlider.setValue(2)
        self.assertAlmostEqual(self.form.getLiters(), 0.0444 * 2)
        print('*** testCase test_liters end ***')
#继承自QThread类
class BackWorkThread(QThread):
    #声明一个信号，同时返回一个str
    finishSignal = pyqtSignal(str)
    #在构造函数中增加形参
    def __init__(self, sleepTime,parent=None):
        super(BackWorkThread, self).__init__(parent)
        #存储参数
        self.sleepTime= sleepTime
        
    #重写run函数，在里面定时执行业务
    def run(self):
        #休眠一段时间
        time.sleep(self.sleepTime)
        #休眠结束，发送一个信号告诉主线程窗口
        self.finishSignal.emit('ok, begin to close Window')
        

if __name__ == '__main__':
    suite = unittest.TestSuite()
#    suite.addTest(MatrixWinTest("test_defaults"))
#    suite.addTest(MatrixWinTest("test_moveScrollBar"))
#    suite.addTest(MatrixWinTest("test_tripleSecSpinBox"))
#    suite.addTest(MatrixWinTest("test_limeJuiceLineEdit"))
#    suite.addTest(MatrixWinTest("test_iceHorizontalSlider"))
#    suite.addTest(MatrixWinTest("test_blenderSpeedButtons"))
    suite.addTest(MatrixWinTest("test_liters"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
