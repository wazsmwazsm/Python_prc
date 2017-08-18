#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name
    # 打印方法类重载
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__


print(Student('Michael'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
    # 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    # for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    # 像 list 一样由下标取数据
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

for n in Fib():
    print(n)

f = Fib()
print(f[1])
print(f[10])
