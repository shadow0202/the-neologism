# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/18 16:24 
# @Software: PyCharm
"""
import os

from pages import page_douban, page_movie, page_esports, page_news, page_sinablog, page_sports, page_toutiao

print("--------------#### 任务正在启动 ####-----------------")

fpath = os.path.dirname(os.path.abspath(__file__))+'\\result\\'

path_list=['douban','esports','movie','news','sinablog','sports','toutiao']


for path in path_list:
    final_path = fpath + path +".txt"
    if os.path.exists(final_path):
        os.remove(final_path)

# 爬取豆瓣信息
print("——————开始爬取豆瓣内容———————")
page_douban.doubanCrawler(fpath+'douban.txt')
# 爬取电竞信息
print("——————开始爬取电竞内容———————")
page_esports.esportsCrawler(fpath+'esports.txt')
# 爬取电影信息
print("——————开始爬取电影内容———————")
page_movie.hotmovieCrawler(fpath+'movie.txt')
# 爬取新闻信息
print("——————开始爬取新闻内容———————")
page_news.newsCrawler(fpath+'news.txt')
# # 爬取微博信息
print("——————开始爬取新浪内容———————")
page_sinablog.sinaCrawler(fpath+'sinablog.txt')
# # 爬取体育信息
print("——————开始爬取体育内容———————")
page_sports.sportCrawler(fpath+'sports.txt')
# 爬取头条信息
print("——————开始爬取头条内容———————")
page_toutiao.toutiaoCrawler(fpath+'toutiao.txt')

