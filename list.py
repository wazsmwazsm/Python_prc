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
