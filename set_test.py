#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# 重复元素会自动去重
s = set([1, 1, 2, 2, 3, 3])

print(s)

s.add(5)
print(s)

s.remove(2)
print(s)

# 交集 并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print(s1 & s2)
print(s1 | s2)
