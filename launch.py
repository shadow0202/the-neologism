# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/18 16:24 
# @Software: PyCharm
"""
import os

from pages import page_douban

fpath = r'./Chinese_segment_augment/data/'

path_list=['douban','esports','movie','news','sinablog','sports','toutiao']

for path in path_list:
    final_path = fpath + path +".txt"
    if os.path.exists(final_path):
        os.remove(final_path)


