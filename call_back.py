#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

print(type(abs))
print(abs)

# 可以给变量赋值函数
x = abs
print(x(-10))

# 函数名是个变量
# abs = -10
# print(abs)


# 高阶函数 (回调函数)
def add(x, y, f):
    return f(x) + f(y)

print(add(-1, -2, abs))
