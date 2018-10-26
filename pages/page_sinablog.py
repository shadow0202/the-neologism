# -*- coding: utf-8 -*-
"""
# @Author  : huxw
# @Update  : 2018/10/16 14:02
# @Software: PyCharm
"""

# 爬取内容：
#     微博信息流
#     热搜以及相关微博
#

import json

from tokenizer.utils import format_str
from utils import download_page

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

def sinaCrawler(path):
    # a、微博信息流、热搜
    hot_tag= []
    hot_tag.append("realtimehot")
    hot_tag.append("socialevent")
    # 写入文件
    file = open(path, "a",encoding="utf-8")
    for tag in hot_tag:
        soup = download_page.download_soup_waitting("https://s.weibo.com/top/summary?cate="+tag,headers,1)
        try:
            hot_list = soup.find_all('td',attrs={"class":"td-02"})
            for hot in hot_list:
                title = hot.find("a").get_text()
                href = "https://s.weibo.com"+hot.find("a").get('href')
                file.write(format_str(title))
                print(title + ":" + href)
                # 过滤无效链接
                if href != "https://s.weibo.comjavascript:void(0);":
                    detail_soup = download_page.download_soup_waitting(href,headers,1)
                    # print(detail_soup)
                    cards = detail_soup.find_all("div",attrs={"class":"card-feed"})
                    for card in cards:
                        content = card.find("div",attrs = {"class":"content"})
                        blogger = content.find("p", attrs={"class": "txt"}).get('nick-name')
                        blog = content.find("p", attrs={"class": "txt"}).get_text()
                        file.write(format_str(blogger+":"+blog))
                        print(blogger+":"+blog)
        except Exception as e:
            print("Except——新浪:爬取异常，已跳过",e)

    # b、微博信息流
    url_hotfeed = "https://api.weibo.cn/2/guest/cardlist?gsid=_2AkMu5Br-f8NhqwJRmPAcz2PmZYl_yQ3EieKYuOslJRM3HRl-3T9kqnwvtRWwLB-1C2SEmptvAP1Bfy0s7kgEgw..&uid=1008938494835&wm=3333_2001&i=8bb4ee5&b=1&from=1073193010&checktoken=807ca79ae3fa897b262e3b63c3882698&c=iphone&networktype=wifi&v_p=45&skin=default&s=ee9f63c1&v_f=1&did=eb4621d547f0e7cb9eef4a41403ee866&lang=zh_CN&sflag=1&ua=iPhone9,2__weibo__7.3.1__iphone__os10.3.1&aid=01AhjayctpFPjOzJEmy46JLMop9TgsXKgsxZQYIpcPoBa-nn8.&lon=116.2697240292689&count=20&fid=230584&containerid=230584&uicode=10000011&lat=40.04127809492162&offset=1&max_id=4151604225452173&page=1&moduleID=pagecard"
    url_starfeed = "https://api.weibo.cn/2/guest/cardlist?gsid=_2AkMu5WfMf8NhqwJRmPAcz2PmZYl_yQ3EieKYuZYXJRM3HRl-3T9kqnZftRVqWDRdwTGKDWtA7iBOAX-N3elOcA..&uid=1008938494835&wm=3333_2001&i=8bb4ee5&b=1&from=1073193010&checktoken=807ca79ae3fa897b262e3b63c3882698&c=iphone&networktype=wifi&v_p=45&skin=default&s=ee9f63c1&v_f=1&did=eb4621d547f0e7cb9eef4a41403ee866&lang=zh_CN&sflag=1&ua=iPhone9,2__weibo__7.3.1__iphone__os10.3.1&aid=01AhjayctpFPjOzJEmy46JLMop9TgsXKgsxZQYIpcPoBa-nn8.&lon=116.2697240292689&count=20&fid=230781&containerid=230781&uicode=10000011&lat=40.04127809492162&offset=1&max_id=4140648884038081&page=1&moduleID=pagecard"
    urlcol = []
    urlcol.append(url_hotfeed)
    urlcol.append(url_starfeed)
    for url in urlcol:
        print ("正在获取微博信息流...")
        res = download_page.download_html_waitting(url,headers,1)
        try:
            res = json.loads(res)
            for cards in res["cards"]:
                # print cards
                if cards["card_type"] == 9:
                    if "text" in cards["mblog"]:
                        # print cards["mblog"]["text"]
                        file.write(cards["mblog"]["text"])
                        print(cards["mblog"]["text"])
        except KeyError as e:
            print ("Except——新浪: " + str(e))

    file.close()




