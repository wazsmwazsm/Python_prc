#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

classmates = ('Michael', 'Bob', 'Tracy')

# 只有一个元素的写法

t = (1,)
print(t)

# 元组中有 list，list 元素可变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
