#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
# 取索引
print(classmates[1])
print(classmates[-1])
print(classmates[-2])

# 嵌套
s = [1,2,[3,4]]
print(s, len(s), s[2][1])

# slice 切片
a = [1,2,3,4,5]
print(a[0:4])

# list 合并
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print(squares)

# 删除元素
del squares[2]
print(squares)

# 内置函数
a = [1,4,3,2,5,6,4,3]
print(len(a), min(a), max(a))

# list 方法
print(a.count(4))

# 结尾追加元素
classmates.append('Adam')
print(classmates)

# 指定索引插入元素
classmates.insert(1, 'Jack')
print(classmates)

# 从尾部移除一个元素
classmates.pop()
print(classmates)

# 移除指定索引元素
classmates.pop(2)
print(classmates)

# 合并一个列表，类似 +
classmates.extend(a)
print(classmates)

# 着粗牧歌值第一个匹配的索引位置
print(a.index(5))

# 反转
a.reverse()
print(a)

# 排序，可传自定义回调函数
a.sort()
print(a)

# 拷贝列表
b = a.copy()
print(b)

# 清除列表
b.clear()
print(b)

# 不拷贝直接赋值的话，是添加数据引用，clear 后都没数据了
b = a;
print(a,b)
a.clear()
print(a)
print(b)
