# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/18 16:54 
# @Software: PyCharm
"""
import requests
from bs4 import BeautifulSoup


def get_ip_list(headers):
    """ 从代理网站上获取代理"""
    print("qwe")
    ip_list = []
    page = requests.get('http://www.xicidaili.com/wt', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    ul_list = soup.find_all('tr', limit=20)
    print(len(ul_list))
    for i in range(2, len(ul_list)):
        line = ul_list[i].find_all('td')
        ip = line[1].text
        port = line[2].text
        address = ip + ':' + port
        ip_list.append(address)
    return ip_list


def get_proxy(aip):
    """构建格式化的单个proxies"""
    proxy_ip = 'http://' + aip
    proxy_ips = 'https://' + aip
    proxy = {'https': proxy_ips, 'http': proxy_ip}
    return proxy



# if __name__ == '__main__':
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
#
#     a = get_ip_list(headers)
#     print(a)