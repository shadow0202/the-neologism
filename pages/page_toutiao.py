# -*- coding: utf-8 -*-
"""
# @Author  : huxw
# @Update  : 2018/10/17 10:33
# @Software: PyCharm
"""

##爬取今日头条频道数据
import requests
import re
import json
import random
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pandas as pd

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  ###禁止提醒SSL警告
import hashlib
import execjs


class toutiao(object):
    def __init__(self, path, url):
        self.path = path  # CSV保存地址
        self.url = url
        self.s = requests.session()
        headers = {'Accept': '*/*',
                   'Accept-Language': 'zh-CN',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
                   'Connection': 'Keep-Alive',

                   }
        self.s.headers.update(headers)
        self.channel = re.search('ch/(.*?)/', url).group(1)

    def closes(self):
        self.s.close()

    def getdata(self):  # 获取数据
        req = self.s.get(url=self.url, verify=False)
        headers = {'referer': self.url}
        max_behot_time = '0'
        signature = '.1.hXgAApDNVcKHe5jmqy.9f4U'
        eas = 'A1E56B6786B47FE'
        ecp = '5B7674A7FF2E9E1'
        self.s.headers.update(headers)

        titles = []
        abstracts = []
        for i in range(0, 10):
            Honey = json.loads(self.get_js())
            eas = Honey['as']
            ecp = Honey['cp']
            signature = Honey['_signature']
            url = 'https://www.toutiao.com/api/pc/feed/?category={}&utm_source=toutiao&widen=1&max_behot_time={}&max_behot_time_tmp={}&tadrequire=true&as={}&cp={}&_signature={}'.format(
                self.channel, max_behot_time, max_behot_time, eas, ecp, signature)
            req = self.s.get(url=url, verify=False)
            time.sleep(random.random() * 2 + 2)
            # print(req.text)
            print(url)
            j = json.loads(req.text)

            items = j['data']
            for item in items:
                try:
                    title = item['title']
                    abstract = item['abstract']
                    print(title + " : " + abstract)
                    titles.append(title)  ##标题
                    try:
                        abstracts.append(abstract)  ###文章摘要
                    except:
                        abstracts.append('')
                except:
                    print("Except - 头条")
            time.sleep(2)

            print('------------' + str(j['next']['max_behot_time']))

            data = {'title': titles, 'abstract': abstracts}
            df = pd.DataFrame(data=data)
            df.to_csv(self.path + r'\toutiao.csv', encoding='GB18030', index=0)

    def getHoney(self, t):  #####根据JS脚本破解as ,cp
        t(t)
        e = str('%X' % t)
        m1 = hashlib.md5()
        m1.update(str(t).encode(encoding='utf-8'))
        i = str(m1.hexdigest()).upper()
        n = i[0:5]
        a = i[-5:]
        s = ''
        r = ''
        for x in range(0, 5):
            s += n[x] + e[x]
            r += e[x + 3] + a[x]
        eas = 'A1' + s + e[-3:]
        ecp = e[0:3] + r + 'E1'
        # printcp)
        return eas, ecp

    def get_js(self):  ###大牛破解as ,cp,  _signature  参数的代码，然而具体关系不确定，不能连续爬取
        f = open(r"C:\Users\huxw\Desktop\the-neologism\utils\toutiao.js", 'r', encoding='UTF-8')
        line = f.readline()
        htmlstr = ''
        while line:
            htmlstr = htmlstr + line
            line = f.readline()
        ctx = execjs.compile(htmlstr)
        return ctx.call('get_as_cp_signature')


if __name__ == '__main__':
    path = r'D:\new'  ##保存路径
    tags = []
    tags.append('news_entertainment/')
    tags.append('news_hot/')
    for tag in tags:
        url = 'https://www.toutiao.com/ch/' + tag  ##频道URL
        t = toutiao(path, url)
        t.getdata()
        t.closes()