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

# 多个循环组合
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

rst = [x*y for x in vec1 for y in vec2]
print(rst)

rst = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(rst)
# 列表推导式可以使用复杂表达式或嵌套函数：
rst = [str(round(355/113, i)) for i in range(1, 6)]
print(rst)
