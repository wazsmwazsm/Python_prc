#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 用 埃氏筛法 求素数

# 得到一个 3 开始的基数序列（去掉了 2 为倍数的）
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 筛选函数 筛选各种倍数的数
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
