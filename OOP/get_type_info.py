#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# types 模块
import types

# type 函数
print(type(123))
print(type('sss'))
print(type(None))
print(type(int))
print(type(123) == type(456))

def fn():
    pass

print(type(fn) == types.FunctionType)   # 是否为函数
print(type(abs) == types.BuiltinFunctionType)   # 是否为内建函数
print(type(lambda x : x) == types.LambdaType)  # 是否是匿名函数
print(type((x for x in range(10))) == types.GeneratorType)  # 是否是生成器

# isinstance 函数
class A(object):
    def __init__(self):
        pass

class B(A):
    pass

a = A()
b = B()
print(isinstance(b, A))
print(isinstance(a, object))
print(isinstance(b, object))

# 判断是否属于两种类型的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# dir 函数
print(dir('ABC'))
# 在len()函数内部，它自动去调用该对象的__len__()方法
print(len('ABC'))
print('ABC'.__len__()) # 和上面等价

# 自己可以重写 object 类原有的方法
class MyDog(object):
    def __len__(self):
        return 100

print(len(MyDog())) # 传一个实例进去

# getattr()、setattr()以及hasattr()
# 由于动态语言的鸭子模型，需要对输入的参数进行类型检查

class MyObj(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObj()

# 属性信息
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(getattr(obj, 'y'))
print(obj.y)
# 方法信息
print(hasattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())
