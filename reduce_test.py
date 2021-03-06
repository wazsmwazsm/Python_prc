#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from functools import reduce

def fn(x, y):
    return x * 10 + y

# reduce(f, [x1, x2, x3, x4]) <===> f(f(f(x1, x2), x3), x4)
print(reduce(fn, [1, 3, 5, 7, 9]))

# 把 str 转换为 int 的函数

def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))

print(str2int('65535'))

# 用 lambda 匿名函数简化
def str2int(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('7788565'))

# 编写 str2float 函数
# 思路 ：1234567 / 10000 = 123.4567 取得小数点的位置就好

def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    if(s.find('-') == 0):
        neg = -1
        s = s[s.index('-') + 1:]
    else:
        neg = 1

    idot = s.index('.')
    num = s[:idot] +  s[idot+1:]
    deno = (10 ** (len(s) - idot - 1))
    return reduce(lambda x, y: x * 10 + y, map(char2num, num)) * neg / deno

print(str2float('-52.535634'))
print(str2float('12.0045'))
