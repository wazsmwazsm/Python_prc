#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'tom'
s.age = 23
# s.gender = 'male' # 报错
print(s.name, s.age)
