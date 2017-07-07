#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)

for x in range(1,40,2):
    print(x)

# for in else

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

# 对字符串进行循环 python 中字符串相当于一个 list
for letter in 'Runoob':
    if letter == 'o':
        continue
    print('当前字母 : ', letter)

# 模仿 for 循环
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# items 遍历
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():  # items 取出键和值，单单遍历 dict 只能取到键
    print(k, v)
