#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# 都好会变为空格分隔
print("Hello", "Mr qin", "good morning!")

# 输出中文, windows git bash 设置为 GBK
print("秦先生你好!")

# 输入
name = input('输入你的名字:')

print('hello', name)

# 不换行输出
print('---', end=" ")
print('aaa', end=" ")

# 输出格式美化

s = 'Hello, Runoob'
print(str(s))
print(repr(s))
print(str(1/7))

#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
print(repr(hello))

# repr() 的参数可以是 Python 的任何对象
print(repr((1, 2, ('Google', 'Runoob'))))

# 输出一个平方与立方的表

# 方法 1
for x in range(1, 11):
    # rjust(n) 字符串右对齐并补齐为 n 位
    print(repr(x).rjust(2), repr(x*x).rjust(3), end='')
    print(repr(x*x*x).rjust(4))

# 方法 2
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# zfill
print('12'.zfill(5))
