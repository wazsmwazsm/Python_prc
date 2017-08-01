#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from collections import Iterable, Iterator

# 查看是否能迭代
print(isinstance('abc', Iterable))   # True
print(isinstance([1,2,3], Iterable)) # True
print(isinstance(123, Iterable))     # False

# 是否是迭代器
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(iter('abc'), Iterator))

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

# 防止死循环，用 StopIteration 来停止迭代
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# generator 生成器

# 简单的生成器
g = (x * x for x in range(10))
print(type(g))
print(next(g))
print(next(g))
# 生成器也是可迭代对象
for i in g:
    print(i)

# 另一种定义生成器的方法 ： 生成器函数
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a # 每次运行到此都返回 a (next 函数调用时返回)
        a, b = b, a + b
        counter += 1

f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
# print 的时候无法这样做，现在可以直接迭代了
for i in fibonacci(10):
    print(i)



# 防止死循环，用 StopIteration 来停止迭代

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 生成器中没有 return 返回值的时候要这么做
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
