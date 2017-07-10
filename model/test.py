#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import sys
import fibo
# 部分引入
from fibo import fib, fib2

# 查看模块的路径
print(sys.path)

for i in fib(10):
    print(i)

# 获得模块定义的所有名称
print(dir(fibo))
print(dir(sys))

# 没有参数则返回当前定义的名称
print(dir())
a = 1
print(dir())
def aa():
    pass
    
print(dir())
