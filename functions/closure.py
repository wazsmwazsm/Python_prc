#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())



# 闭包中的循环不是每次都保存 编译后只剩下最后的
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

# 解决这个问题可以不用循环，或者再包裹一次
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count2()
print(f1(),f2(),f3())
