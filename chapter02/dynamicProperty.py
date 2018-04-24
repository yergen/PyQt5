# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:12:18 2018

@author: Administrator
"""

#如果不希望类的某属性被悄悄地访问、赋值或修改，希望在被访问、赋值或修改时得到一些通知，
#那么可以使用函数property()。
#方法一
class MyClass(object):
    def __init__(self):
        self._param = None
    
    def getParam(self):
        print("get param: %s" % self._param)
        return self._param
    
    def setParam(self,value):
        print("set param: %s" % self._param)
        self._param = value
    
    def delParam(self):
        print("delete param: %s" % self._param)
        del self._param
    
    param = property(getParam, setParam, delParam)
    
if __name__ == "__main__":
    cls = MyClass()
    cls.param = 10
    print('current param是：%d' % cls.param)
    del cls.param