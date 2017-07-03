#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

list=[1,2,3,4]

# 创建迭代器对象
it = iter(list)
print(next(it))
print(next(it))

# 用循环遍历迭代器对象
it = iter(list)
for x in it:
    print(x, end='')

print('\n')
# 迭代一个迭代器对象

import sys
list=[5,6,7,8]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

# generator 生成器

# 生成器函数 - 斐波那契
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a # 每次运行到此都返回 a (next 函数调用时返回)
        a, b = b, a + b
        counter += 1

f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
