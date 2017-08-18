#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class Student(object):
    # getter 方法
    @property
    def score(self):
        return self._score
    # setter 方法
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger !')
        if value < 0 or value  > 100:
            raise ValueError('score must between 0~100 !')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

s = Student()
s.score = 60
# s.score = '60'
# s.score = 110
s.birth = 1992
print(s.age)
# 没有 setter 为只读属性，不可设置
# s.age = 12
