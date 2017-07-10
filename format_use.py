#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import math

# 基本使用
print('姓名：{}，性别：{}'.format('秦先生', '男'))
# 指定位置
print('姓名：{1}，性别：{0}'.format('男', '秦先生'))

# 关键字参数
print('姓名：{name}，性别：{gender}'.format(name = '秦先生', gender = '男'))

# 组合使用, 位置参数要在前面哦
print('姓名：{name}，性别：{gender}，年龄{0}'.format(26, name = '秦先生', gender = '男'))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print('常量 PI 的值近似为： {!r}。'.format(math.pi))

# 可选项 ':' 和格式标识符可以跟着字段名, .3f 表示保留到小数点后三位
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

# 传入一个字典, 然后使用方括号 '[]' 来访问键值 {0[key]} 因为之传入了一个值，用 0 代表变量 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# 这里的 0 是 table
print('Runoob : {0[Runoob]:d}; Google : {0[Google]:d}; Taobao : {0[Taobao]:d}'.format(table))

# 使用 ** 来传 dict
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob : {Runoob:d}; Google : {Google:d}; Taobao : {Taobao:d}'.format(**table))
