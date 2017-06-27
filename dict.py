#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

score = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}

# 注意， python2.7 会输出括号 3 不会
print("score['Michael'] = ", score['Michael'])

# get 方法可以返回一个默认值
print(score.get('aa', -1))

# 删除元素
score.pop('Tracy');
print(score)

# 判断 key 值在不在 dict 中
print('aa' in score)
