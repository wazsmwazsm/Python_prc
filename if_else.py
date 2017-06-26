#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# 注意 stdin 接收到的数据是 string　类型的
birth = input('生日年份:')
birth = int(birth)
if birth >= 2000 :
    print("00 后")
elif 1990 <= birth < 2000 :
    print("90 后")
else :
    print("中年人")
