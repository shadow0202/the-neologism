# -*- coding:utf-8 -*-
"""
# @Author  : huxw
# @Update  : 2018/10/16 14:02
# @Software: PyCharm
"""

import requests
import time
from bs4 import BeautifulSoup



# 返回soup，便于解析
def download_soup_waitting(url,headers,num):
    try:
        response= requests.get(url,headers=headers,allow_redirects=False,timeout=5)
        if response.status_code==200:
            html=response.content
            soup = BeautifulSoup(html, "html.parser")
            return soup
        else:
            # 等待五秒，链接异常直接跳往下一链接
            if num < 5 :
                time.sleep(1)
                print("正在爬取该页面:"+url+"")
                return download_soup_waitting(url,num + 1)
            else:
                print ('该链接异常')
    except:
        return "none"


# 返回页面内容，适用于接口形式的json字符串
def download_html_waitting(url,headers,num):
    try:
        response= requests.get(url,headers=headers,allow_redirects=False,timeout=5)
        if response.status_code==200:
            html=response.content
            return html
        else:
            # 等待五秒，链接异常直接跳往下一链接
            if num < 5 :
                time.sleep(1)
                print("正在爬取该页面:"+url+"")
                return download_html_waitting(url,num + 1)
            else:
                print ('该链接异常')
    except:
        return "none"