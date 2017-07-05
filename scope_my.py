#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# if/elif/else/、try/except、for/while 不会引入新作用域
if True:
    msg = 'hahahahhahahaha'

print(msg)


# 修改了内建变量，作用域先查找自定义的，最后查找内建的
__file__ = '1'
print(__file__)

# 全局变量
total = 0

def sum(a, b):
    total = a + b    # 读取是没问题了，但是不能修改
    print("函数内是局部变量 : ", total)
    return total

sum(10, 20)
print ("函数外是全局变量 : ", total)

# global 关键字
num = 1
def fun1():
    global num  # 声明全局变量后，就可以修改啦
    print(num)
    num = 123
    print(num)

fun1()
print(num)

# globals()
num = 1
def fun1():
    print(num)
    globals()['num'] = 123 # 使用 globals 直接获取全局变量
    print(num)

fun1()
print(num)

# nonlocal 关键字
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
    
outer()

# locals() 获取所有的局部参数, 打包成一个 dict
def aa():
    a = 1
    b = 2
    c = 3
    print(locals())

aa()
