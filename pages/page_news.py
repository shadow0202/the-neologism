# -*- coding: utf-8 -*-
"""
# @Author  : huxw
# @Update  : 2018/10/16 14:02
# @Software: PyCharm
"""

# 爬取内容：
#  国内、国际、社会类新闻
import json

from utils import download_page

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

def newsCrawler():
    tags = ['china','society','world']
    for tag in tags:
        url = r'http://news.cctv.com/' + tag + r'/data/index.json'
        result = download_page.download_html_waitting(url,headers,1)
        result = json.loads(result,strict=False)
        result = result['rollData']
        for item in result:
            title = item["title"]
            url = item['url']
            try:
                soup = download_page.download_soup_waitting(url,headers,1)
                content = soup.find('div', {'class': 'cnt_bd'})
                # 剔除无关标签
                [s.extract() for s in content(['div', 'script'])]
                # print title, content.get_text().strip().replace('\n', '')
                result = title + ":" + content.get_text().strip().replace('\n', '')
                print(result)
            except:
                print ("Except - 新闻:"+url)
