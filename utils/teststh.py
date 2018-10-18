# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/18 16:11 
# @Software: PyCharm
"""
import os

filepath = r'../Chinese_segment_augment/data/test'

if os.path.exists(filepath):
    os.remove(filepath)

f = open(filepath, "a")
for i in range(45,1111):
    f.write(str(i))