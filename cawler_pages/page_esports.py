# -*- coding: utf-8 -*-
"""
# @Author  : huxw
# @Update  : 2018/10/16 14:02
# @Software: PyCharm
"""

# 爬取内容：
#     a、最新电竞信息
import json

from new_word_md.utils import format_str
from utils import download_page

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

def esportsCrawler(path):
    for i in range(1,10):
        url = 'http://www.dadianjing.cn/index.php?m=Index&a=xhrList&cid=1&page='+str(i)
        try:
            result = download_page.download_html_waitting(url, headers, 1)
            result = json.loads(result,strict=False)
            items = result["data"]["list"]
            # 写入文件
            file = open(path, "a",encoding="utf-8")
            file.write("抓取电竞内容")
            for item in items:
                title = item['title']
                summary = item['summary']
                file.write(format_str((title+":"+summary))+'\n')
                print(title + "---" + summary)
            file.close()
        except Exception as e:
            print ("Except - 电竞:" + url,e)
    return 'success'

