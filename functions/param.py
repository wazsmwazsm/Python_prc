#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# 位置参数
def power(x):
    return x * x

print(power(5), power(25))

def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print(power(5,3), power(25,2))

# 默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')

# 默认参数的默认值要设置为不可变参数 (不能设置为 list 和 dict)
def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end()) # 当开始不传参数时，会每次都是用默认的 [] 的那个 list 对象
print(add_end()) # 出现数据不对的问题

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

calc()
calc(1,2,3)

# 或者传一个 list 或者 tuple
calc(*[4,5,6])
calc(*(7,8,9))

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city = 'Beijing')
person('Adam', 40, city = 'Shanghai', job = 'winner')
person('Adam', 40, city = 'Shanghai', job = 'winner')
# 关键字参数必须要有键值，不然会被认为是位置参数导致参数不符合而保持
# person('Adam', 40, 'Shanghai', 'winner')
# 也可以传一个 dict
person('Qin', 40, **{'a' : 1, 'b' : 2})

# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Jack', 24, 1,2,3, city='Beijing', job='Engineer')

# 命名关键字参数可以有缺省值，从而简化调用
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')

# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99)
f2(1, 2, d = 99, ext = None)

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
