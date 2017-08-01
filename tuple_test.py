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

# 合并
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

print(tup1 + tup2)

del tup1
# print(tup1)
# 重复
print(tup2 * 3)

tp = (1,2,4,5,66,3)
# 内置函数
print(len(tp), max(tp), min(tp))
