#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

def f(x):
    return x * x

# 接收一个函数和一个迭代器对象
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# 返回的是一个迭代器对象
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
