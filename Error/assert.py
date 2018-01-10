#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

foo('0')

# python -O assert.py 可以关闭断言
