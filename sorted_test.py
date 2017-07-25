#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

print(sorted([36, 5, -12, 9, -21]))

# key 函数指定排序规则
print(sorted([36, 5, -12, 9, -21], key=abs))

# 字符串
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


# 综合
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

print(sorted(L, key=by_name))
print(sorted(L, key=by_score))
