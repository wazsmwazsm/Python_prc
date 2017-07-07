#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# 杨辉三角

# 建立生成器
def triangles(n):
    i = 0
    row = [1]
    while(i < n):
        yield row
        # 最后一个不用算
        row = [1] + [row[x] + row[x+1] for x in range(len(row)-1)] + [1]
        i += 1
for restut in triangles(20):
    print(restut)
# print([restut for restut in triangles(10)])
