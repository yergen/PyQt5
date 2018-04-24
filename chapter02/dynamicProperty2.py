# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:43:08 2018

@author: Administrator
"""

class MyClass(object):
    def __init__(self):
        self._param = None
        
    @property
    def param(self):
        print("get param: %s" % self._param)
        return self._param
    
    @param.setter
    def param(self,value):
        print("set param: %s" % self._param)
        self._param = value
    
    @param.deleter
    def param(self):
        print("delete param:%s" % self._param)
        del self._param

if __name__ == "__main__":
    cls = MyClass()
    cls.param = 12
    print("current param: %s" % cls.param)
    del cls.param