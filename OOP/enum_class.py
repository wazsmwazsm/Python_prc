#! /usr/bin/env python3
#! -*- coding:UTF-8 -*-

from enum import Enum, unique
# 用来处理常量定义
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'));

print(Month.Jan)
print(Month.Jan.value)
# 遍历所有元素
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 从 Enum 派生出自定义类
@unique  # @unique 装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)

for name, member in Weekday.__members__.items():
    print(name, '=>', member, 'value:', member.value)
