# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/16 16:18 
# @Software: PyCharm
"""

# 爬取内容：
#     24小时话题以及热评
#     热门电脑影评

import json
import re
import telnetlib

import requests
from bs4 import BeautifulSoup

from utils import download_page, ipAgency
from utils.ipAgency import get_proxy

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

def doubanCrawler(path):
    # 获取代理IP
    ip_list = ipAgency.get_ip_list(headers)
    for ip in ip_list:
        hd, port = ip.split(':')
        try:
            telnetlib.Telnet(hd, port=port, timeout=20)
        except:
            print(str(ip)+'失败')
        else:
            proxies = get_proxy(ip)
                # 伪造cookie
            jar = requests.cookies.RequestsCookieJar()
            jar.set('bid', 'ehjk9OLdwha', domain='.douban.com', path='/')
            jar.set('11', '25678', domain='.douban.com', path='/')
            html = requests.get("https://www.douban.com/gallery/",cookies=jar,proxies=proxies,headers = headers)
            html = html.content
            soup = BeautifulSoup(html, "html.parser")
            print(soup)
            hot_topics = soup.find("ul",attrs={"class":"trend"}).find_all("li")
            file = open(path, "a")
            for topic in hot_topics:
                try:
                    title =topic.find('a').get_text()
                    href = topic.find('a').get('href')
                    print(title,href)
                    headers2={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                            'Referer':href}
                    com_id = re.findall("\d+", href)[0]
                    nums=["0","20","40"]
                    for num in nums:
                        url="https://m.douban.com/rexxar/api/v2/gallery/topic/"+str(com_id)+"/items?sort=hot&start=0&count="+num+"&status_full_text=1&guest_only=0&ck=null"
                        try:
                            html = download_page.download_html_waitting(url,headers2,1)
                            res = json.loads(html)
                            for item in res["items"]:
                                file.write(item["abstract"])
                                print(item["abstract"])
                        except:
                            print("Except——豆瓣:爬取热评失败")
                except:
                    print("Except——豆瓣:爬取24小时热门话题失败")
            file.close()
            break

            # 影评
            # TODO 优先级不高。做了一个单独爬电影和简介的movieCrawler()



