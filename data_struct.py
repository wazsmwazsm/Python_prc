#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# stack

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)

print(stack.pop())

print(stack)

# queue
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue)

# 列表推导式

vec = [2, 4, 6]

rst = [x * 3 for x in vec] # [] 返回一个 list
# rst = {x * 3 for x in vec} {} 返回一个 set
print(rst)

# 生成多个元素
rst = [[x, x**2] for x in vec]
print(rst)

# 对序列中每一个元素逐个调用方法
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
rst = [weapon.strip() for weapon in freshfruit]
print(rst)

# if 子句作为过滤器
rst = [3*x for x in vec if x > 3]
print(rst)

# 多个循环组合，相当于嵌套循环
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

rst = [x*y for x in vec1 for y in vec2]
print(rst)

rst = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(rst)
# 列表推导式可以使用复杂表达式或嵌套函数：
rst = [str(round(355/113, i)) for i in range(1, 6)]
print(rst)

# 列表嵌套
# 矩阵行列转换
matrix = [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
]
# 嵌套使用运算式
rst = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(rst)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

# 最原始的方法
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
# del 语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)

# 元组
# 定义时可以不加圆括号，但是最好加上
t = 12345, 54321, 'hello!'
print(t)

# 集合也可使用推导式
# 输出为集合
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# dict
# 直接指定键值对儿
a = dict(sape=4139, guido=4127, jack=4098)
print(a)

# dict 推导式
rst = {x: x**2 for x in (2,4,5)}
print(rst)

# 遍历 dict 值
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():  # items 取出键和值，单单遍历 dict 只能取到键
    print(k, v)

# 获取索引和值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 遍历多个
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue', 'you'] # 会忽略多余的元素
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
