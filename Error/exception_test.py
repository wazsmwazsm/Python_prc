#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import sys

# try catch
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print('Oops!  That was no valid number.  Try again   ')

# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
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

# else 语句
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('不能打开', arg)
    else:
        print(arg, '有', len(f.readlines()), '行')
        f.close()

# try catch 可以捕捉到函数中的异常
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# 抛出一个指定异常
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise # 继续向上层抛出异常

# 自定义异常 继承自 Exception
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e)

# 定义清理行为 finally
try:
    raise KeyboardInterrupt
finally:  # 异常会在 finally 子句执行后再次被抛出给外层
    print('再见！')

# 综合的一个例子
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('0 作为除数！')
    else:
        print('结果是：', result)
    finally:
        print("异常处理结束")

divide(2, 1)
divide(2, 0)
divide("2", "1")

# 预定义的清理行为 with
with open('myfile.txt') as f:
    for line in f:
        print(line, end="")
