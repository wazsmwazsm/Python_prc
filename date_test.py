#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import time
import calendar

print("当前时间戳为:", time.time())
print("当前时间为:", time.localtime(time.time())) # 得到时间元组

# 获取格式化时间

# asctime
print("本地时间为:", time.asctime(time.localtime(time.time()))) #

# 手动格式化
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化时间字符串转化为时间戳

a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 获取日历
cal = calendar.month(2017, 8)
print ("以下输出 2017 年 8 月份的日历:")
print (cal)
