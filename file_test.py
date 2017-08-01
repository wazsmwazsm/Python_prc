#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


# 打开、写入
f = open('./foo.txt', 'a+')
# 返回写入的字符数
num = f.write("Hello world")
print(num)
f.close()

# 读取一行
f = open('./foo.txt', 'r')

str = f.readline()
print(str)

f.close()

# 读取所有行
f = open('./foo.txt', 'r')

lines = f.readlines()
print(lines)

f.close()

# 直接迭代
f = open('./foo.txt', 'r')

for line in f:
    print(line)

f.close()

# seek tell

"""
    f.seek()
    如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
    from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
    seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    seek(x,1) ： 表示从当前位置往后移动x个字符
    seek(-x,2)：表示从文件的结尾往前移动x个字符
"""

f = open('./foo.txt', 'rb+')
# print(f.write(b'0123456789abcdef'))

print(f.tell())

print(f.seek(5)) # 移动到文件的第六个字节
print(f.read(1)) # 读取
print(f.seek(-3, 2)) # 移动到文件的倒数第三字节
print(f.read(1))
