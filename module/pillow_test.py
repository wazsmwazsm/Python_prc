#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
from PIL import Image

im = Image.open('basic_41.jpg')
print(im)
im.thumbnail((200,200))
im.save('thumb.png', 'PNG')
