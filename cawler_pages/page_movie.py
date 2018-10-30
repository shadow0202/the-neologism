# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/18 15:14 
# @Software: PyCharm
"""

#  爬取内容：
#    豆瓣电影
#
import json
import telnetlib
import time

import requests
from bs4 import BeautifulSoup

from new_word_md.utils import format_str
from utils import download_page, ipAgency
from utils.ipAgency import get_proxy

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
headers['Cookie'] = 'bid=T49xdwTmZY4; ll="108288"; __yadk_uid=woHE3QgMUL23JoUFUiyuDxMzsfgc5It1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17471; _vwo_uuid_v2=D9D3712284AFA69C60840BB052A1BB187|5a281aec8be6c06bc612cfecc841a010; ct=y; __utma=30149280.1227353955.1517381502.1521529769.1521534968.19; __utmz=30149280.1521534968.19.16.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1064529217.1517469969.1521106834.1521535037.7; __utmb=223695111.0.10.1521535037; __utmz=223695111.1521535037.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1521535037%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Djz5Q6vo50cs3NxdSUtDbwVKCLL_8iWMOYZnYLWM4fZAeQZEU3PWMwECl63LE--rY%26wd%3D%26eqid%3Df4bbea420001ecdb000000035ab0c7f4%22%5D; _pk_id.100001.4cf6=f4c899e363d94597.1517469969.7.1521535037.1521106841.; _pk_ses.100001.4cf6=*; ps=y; __utmc=30149280; __utmt=1; __utmb=30149280.9.6.1521534968; dbcl2="174712879:Icg9kH/qLsI"; ck=kuI4'


def hotmovieCrawler(path):
    start = 0
    # 不断请求，直到返回结果为
    file = open(path, "a", encoding="utf-8")
    while start <= 40:
        # 拼接需要请求的链接，包括标签和开始编号
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=' + str(
            start)
        result = download_page.download_html_waitting(url, headers, 1)
        if result != "none":
            print("-------------没有使用代理---------------")
            result = json.loads(result)
            movie_items = result['subjects']
            for movie_item in movie_items:
                movie_url = movie_item['url']
                # 提取电影简介
                # 捕捉异常，有的电影详情页中并没有简介
                try:
                    html = requests.get(movie_url).content
                    soup = BeautifulSoup(html, "html.parser")
                    description = soup.find_all("span", attrs={"property": "v:summary"})[0].get_text().strip().replace('\n','')
                    file.write(format_str(description.encode('utf-8', 'ignore').decode('utf-8', 'ignore')) + '\n')
                    print(description)
                except Exception as e:
                    print("该电影没有简介", e)
                time.sleep(0.5)
        else:
            print("-------------使用代理---------------")
            # 获取代理IP
            ip_list = ipAgency.get_ip_list(headers)
            # print(ip_list)
            for ip in ip_list:
                hd, port = ip.split(':')
                try:
                    telnetlib.Telnet(hd, port=port, timeout=20)
                except:
                    print(str(ip) + '失败')
                else:
                    try:
                        proxies = get_proxy(ip)
                        requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
                        s = requests.session()
                        s.keep_alive = False  # 关闭多余连接
                        s.proxies = proxies
                        s.headers = headers
                        html = requests.get(url).content
                        if html == "none":
                            continue
                        result = json.loads(html)
                        movie_items = result['subjects']
                        for movie_item in movie_items:
                            movie_url = movie_item['url']
                            # 提取电影简介
                            # 捕捉异常，有的电影详情页中并没有简介
                            try:
                                html = requests.get(movie_url).content
                                soup = BeautifulSoup(html, "html.parser")
                                description = soup.find_all("span", attrs={"property": "v:summary"})[0].get_text().strip().replace('\n', '')
                                file.write(format_str(description.encode('utf-8', 'ignore').decode('utf-8', 'ignore')) + '\n')
                                print(description)
                            except Exception as e:
                                print("该电影没有简介",e)
                            time.sleep(0.5)
                    except Exception as e:
                        print("Except——电影:", e)

        start += 20
    file.close()
