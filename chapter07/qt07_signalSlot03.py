from PyQt5.QtCore import QObject, pyqtSignal

class SignalClass(QObject):
    #声明无参数的信号
    signal1 = pyqtSignal()
    #声明一个int类型参数的信号
    signal2 = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super(SignalClass, self).__init__(parent)
        
        #将信号signal1连接到sin1Call和sin2Call这两个槽函数
        self.signal1.connect(self.sin1Call)
        self.signal1.connect(self.sin2Call)
        
        #将信号signal2连接到signal1
        self.signal2.connect(self.signal1)
        
        #发射信号
        self.signal1.emit()
        self.signal2.emit(1)
        
        #断开signal、signal2信号与各槽函数的连接
        self.signal1.disconnect(self.sin1Call)
        self.signal1.disconnect(self.sin2Call)
        self.signal2.disconnect(self.signal1)
        
        #将信号signal1和signal2连接到同一个槽函数sin1Call
        self.signal1.connect(self.sin1Call)
        self.signal2.connect(self.sin1Call)
        
        #再次发射信号
        self.signal1.emit()
        self.signal2.emit(1)
        
    def sin1Call(self):
        print("signal-1 emit")
    
    def sin2Call(self):
       print("signal-2 emit") 

if __name__ == "__main__":
    signal = SignalClass()
