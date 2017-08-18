#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
from types import MethodType

class Student:
    pass

def set_score(self, score):
    self.score = score

# 给对象动态绑定属性
stu1 = Student()
stu1.score = 1
print(stu1.score)

# 给类绑定属性
Student.score = 2
stu1 = Student()
stu2 = Student()
print(stu1.score, stu2.score)

# 给实例绑定方法
stu1.set_score = MethodType(set_score, stu1)
stu1.set_score(90)
print(stu1.score)

# 给类绑定方法 这种属于直接把方法增加到类中
Student.set_score = set_score
stu1.set_score(90)
stu2.set_score(88)
print(stu1.score)
print(stu2.score)

# 给类绑定方法二，使用 MethodType
# 这种方法会两个实例只得到一个值
# 因为 MethodType 只是引用了 set_score 函数，函数和内部数据并没有复制到 class 中
# 它不是写在类中的，所以函数中的 self 并不是类的实例，只是一个参数一个局部变量
# 引用时 set_score 函数中的 self.score 被类引用
# 这个数据在 set_score 的那块内存中，只有一份，所以每次调用都会修改
# 当然如果对象本身有属性就不一样了

stu3 = Student()
stu4 = Student()
# stu3.score = 1 # 对象的属性优先于类的和方法绑定中的
# stu4.score = 1
Student.set_score = MethodType(set_score, Student)
stu3.set_score(90)
stu4.set_score(88)
print(stu3.score)
print(stu4.score)
