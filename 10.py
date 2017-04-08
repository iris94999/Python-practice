# coding: utf-8

# 题目：，并格式化当前时间。 暂停一秒输出

import time

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))