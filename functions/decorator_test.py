#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import functools

def log(func):
    # 复制原函数的 __name__ 属性
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 使用装饰器
@log
def now():
    print('2015-3-25')

now()



# 带参数的 decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()
