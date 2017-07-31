#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import functools

int2 = functools.partial(int, base=2)

print(int2('11111111110'))
print(int2('1010101'))
