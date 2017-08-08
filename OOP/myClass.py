#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class MyClass:
    """ 一个简单的类实例 """
    i = 1234
    def f(self):    # self 代表实例
        return 'hello my friend!'

# 实例化类
x = MyClass()

# 访问实例的属性、方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

# 使用构造函数

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def sum(self):
        return self.r + self.i
        
x = Complex(3.0, -4.5)
print(x.sum())
