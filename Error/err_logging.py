#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        # 打印异常并不终止程序执行
        logging.exception(e)

main()
print('END')
