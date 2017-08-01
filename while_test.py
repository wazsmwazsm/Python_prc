#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

sum = 0
n = 1

# 注意，python 和 ruby 一样也没有 ++ 自增自减运算符
while n <= 100:
    sum += n
    n += 1

print(sum)

# while else
count = 0
while count < 5:
    print(count, " 小于 5 ")
    count += 1
else:
    print(count, " 大于等于 5 ")
