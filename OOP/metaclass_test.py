#! /usr/bin/env python3
#! -*- coding:UTF-8 -*-

# type 去创建一个类

'''
要创建一个class对象，type()函数依次传入3个参数：

    1. class的名称；
    2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

'''

def fn(self, name = 'python'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello = fn))

h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# 使用元类 metaclass
# 按照默认习惯，metaclass的类名总是以Metaclass结尾
class ListMetaclass(type):
    '''
    __new__()方法接收到的参数依次是：

        1. 当前准备创建的类的对象；

        2. 类的名字；

        3. 类继承的父类集合；

        4. 类的方法集合。

    '''
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
# metaclass 定义类, 这样可以动态的生产一些类，可以很方便的更具不同的条件
# 建立不同的类
class MyList(list, metaclass = ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)
