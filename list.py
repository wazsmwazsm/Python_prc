#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(classmates[1])
print(classmates[-1])
print(classmates[-2])

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(2)
print(classmates)

s = [1,2,[3,4]]
print(s, len(s), s[2][1])

# slice
a = [1,2,3,4,5]
print(a[0:4])

# list 合并
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print(squares)
