# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/18 16:11 
# @Software: PyCharm
"""
import os

# filepath = r'../Chinese_segment_augment/data/test'
#
# if os.path.exists(filepath):
#     os.remove(filepath)
#
# f = open(filepath, "a")
# for i in range(45,1111):
#     f.write(str(i))

# fos = open("a.txt", "a", encoding="utf-8")
# fos.write("我今年十八岁")
# fos.close()

# print(os.path.abspath(".py"))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.dirname(__file__)))