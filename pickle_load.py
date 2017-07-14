#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import pickle, pprint

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

# 当时 dump 几个进去，就能取几次取回来
data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
