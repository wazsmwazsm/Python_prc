#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# 传不可变对象实例

def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)

# 传可变对象实例
def changeme(mylist):
    mylist.append([1,2,3,4])
    print('函数内的值:', mylist)

mylist = [10,20,30]
changeme(mylist)
print(mylist)
