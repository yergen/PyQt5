# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 09:53:54 2018

@author: Administrator
"""

#类的私有方法：在类的内部使用，命名格式为__private_method。只能在类的内部调用。
#类的私有属性：在类的内部使用，命名格式为__private_attrs。只能在类的内部调用。

class Mycounter:
    __secretCount = 0 #私有变量
    publicCount = 0 #公有变量
    
    def __privateCountFun(self):
        print('这是私有方法__privateCountFun()')
        self.__secretCount = 1
        self.publicCount += 1
        
    def publicCountFun(self):
        print('这是公共方法publicCountFun()')
        self.__privateCountFun() #公共方法调用私有方法

if __name__ == '__main__':
    counter = Mycounter()
    counter.publicCountFun()
    counter.publicCountFun()
    print('instance publicCount=%d' % counter.publicCount)
    print('class publicCount=%d' % Mycounter.publicCount)