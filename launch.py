# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/18 16:24 
# @Software: PyCharm
"""
import os

import new_word_md
from cawler_pages import page_douban, page_movie, page_esports, page_news, page_sinablog, page_sports, page_toutiao
from globalVariable import fpath
from jieba_md import jieba_fenci
from new_word_md import newword
from word_seg_md import newWordsFind

print("--------------#### 任务正在启动 ####-----------------")


path_list=['douban','esports','movie','news','sinablog','sports','toutiao']


# # 清除上次运行结果
# for path in path_list:
#     cawler_res = fpath + '\\cawler_result\\' + path + '.txt'
#     jieba_res = fpath + '\\jieba_md\\result\\' + path + '_result.txt'
#     new_word_res = fpath + '\\new_word_md\\result\\' + path + '_result.txt'
#     word_seg_md = fpath + '\\word_seg_md\\result\\' + path + '_result.txt'
#
#     if os.path.exists(cawler_res):
#         os.remove(cawler_res)
#
#     if os.path.exists(jieba_res):
#         os.remove(jieba_res)
#
#     if os.path.exists(new_word_res):
#         os.remove(new_word_res)
#
#     if os.path.exists(word_seg_md):
#         os.remove(word_seg_md)
#
# final_res = ['\\jieba_md', '\\new_word_md', '\\word_seg_md']
# for res in final_res:
#     if os.path.exists(fpath + res + '\\final_result.txt'):
#         os.remove(fpath + res + '\\final_result.txt')
#
# if os.path.exists(fpath + '\\result\\result.txt'):
#         os.remove(fpath + '\\result\\result.txt')

# 爬取豆瓣信息
# print("——————开始爬取豆瓣内容———————")
# page_douban.doubanCrawler(fpath+'\\cawler_result\\'+'douban.txt')
# # 爬取电竞信息
# print("——————开始爬取电竞内容———————")
# page_esports.esportsCrawler(fpath+'\\cawler_result\\'+'esports.txt')
# # 爬取电影信息
# print("——————开始爬取电影内容———————")
# page_movie.hotmovieCrawler(fpath+'\\cawler_result\\'+'movie.txt')
# # 爬取新闻信息
# print("——————开始爬取新闻内容———————")
# page_news.newsCrawler(fpath+'\\cawler_result\\'+'news.txt')
# # # 爬取微博信息
# print("——————开始爬取新浪内容———————")
# page_sinablog.sinaCrawler(fpath+'\\cawler_result\\'+'sinablog.txt')
# # # 爬取体育信息
# print("——————开始爬取体育内容———————")
# page_sports.sportCrawler(fpath+'\\cawler_result\\'+'sports.txt')
# # 爬取头条信息
# print("——————开始爬取头条内容———————")
# page_toutiao.toutiaoCrawler(fpath+'\\cawler_result\\'+'toutiao.txt')


# 调分词脚本
# jb_res = jieba_fenci.run()
nw_res = newword.run()
# wf_res = newWordsFind.run()

nw_final_res = set(nw_res)
file = open(fpath + '\\result\\result.txt','a',encoding='utf-8')
for res in nw_final_res:
    file.write(res + '\n')

# file.close()

print('--------------#### 任务结束 ####-----------------')