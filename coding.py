#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# python3 默认编码为 unicode

# 单个字符编码
print(ord('A'))
print(chr(66))
print(chr(25991))

# bytes
print(b'ABC')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# len
print(len('中文'))
print(len('中文'.encode('utf-8'))) # bytes 形式计算字节数

# 格式化 和 C 的 printf 一致
print('Hello %s' % 'Qinjiaqi')
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))

'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''

"""
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
"""
