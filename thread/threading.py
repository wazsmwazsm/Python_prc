#!/usr/bin/env python
# coding: utf-8

import threading
import time

def test(i): 
    time.sleep(1)
    print(i)

thread_pool = []
nums = range(1, 10)
start_time = time.time()
# 建立线程
for num in nums:
    t = threading.Thread(target=test,args=(num,))
    t.start()
    thread_pool.append(t)
# 等待线程完成
for t in thread_pool:
    t.join()

end_time = time.time()
