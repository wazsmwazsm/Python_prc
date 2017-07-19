#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print('Oops!  That was no valid number.  Try again   ')

import sys

try:
    f = open('foo.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    # 未存在的名称
    print("OS error: {0}".format(err))
except ValueError:
    # 不合适的数据类型
    print("Could not convert data to an integer.")
except:
    # 其他错误
    print("Unexpected error:", sys.exc_info()[0])
    raise
