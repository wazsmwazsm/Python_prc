#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

score = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}

# 注意， python2.7 会输出括号 3 不会
print("score['Michael'] = ", score['Michael'])

# get 方法可以返回一个默认值
print(score.get('aa', -1))
score.setdefault('aa', 'I\'m aa')
print(score)
# 删除元素
score.pop('Tracy');
print(score)

# 判断 key 值在不在 dict 中
print('aa' in score)

# 删除
del score['Bob']
print(score)
# score.clear()
# print(score)
# del score
# print(score)

# 打印字典
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict)
# 输出字典，以可打印的字符串表示。
print(str(dict))

# dict 方法
print(dict.keys())
print(dict.values())

# 以 list 的形式返回可遍历的(键, 值) 元组数组
print(dict.items())

# 随机删除返回一个键值对 (可用到随机读地址，失效的话继续读取)
print(dict.popitem())

# 深拷贝和浅拷贝 同样适用于 list
a = {'age':11, 'info':{'name':'filex', 'time': '2'}}
print(a)
b = a.copy()

# 修改 a 的顶级元素
a['age'] = 55
print(a)
print(b)  # OK b 没有被修改

# 此时修改 a 的 嵌套元素
a['info']['ss'] = 'a';
# 发现 b 被修改了
print(a)
print(b)

# 使用 深拷贝
import copy

c = copy.deepcopy(a)
# 此时修改 a 的 嵌套元素
a['info']['aa'] = 'a';
# 发现 b 没有被修改
print(a)
print(c)

# 合并 等于 +
a = {'a':1, 'b':2}
b = {'d':4, 'c':3}

b.update(a)
print(b)
