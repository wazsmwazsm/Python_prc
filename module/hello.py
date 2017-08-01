#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# module 的说明
' a test module'
# 作者
__author__ = 'Qinjiaqi'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 只有单独执行时才执行 if 成功的代码
if __name__ == '__main__':
    test()
