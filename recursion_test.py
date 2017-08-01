#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))


# 尾递归优化 python 解释器没有优化，太深还是会溢出
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(6))

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
