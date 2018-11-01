# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/18 16:11 
# @Software: PyCharm
"""
import json
import os

# filepath = r'../Chinese_segment_augment/data/test'
#
# if os.path.exists(filepath):
#     os.remove(filepath)
#
# f = open(filepath, "a")
# for i in range(45,1111):
#     f.write(str(i))

# fos = open("a.txt", "a", encoding="utf-8")
# fos.write("我今年十八岁")
# fos.close()

# print(os.path.abspath(".py"))
# print(os.path.abspath(os.path.join(os.getcwd(), "..")))
# print(os.path.abspath(os.path.dirname(os.getcwd())))
# print(os.path.abspath(os.path.dirname(__file__)))
#
# str = 'abcdefghijklmnopqrstuvwxyz'
# jstr = json.loads(str)
# print(jstr)

# lists=[{'rate': '8.7', 'cover_x': 1400, 'title': '网络谜踪', 'url': 'https://movie.douban.com/subject/27615441/', 'playable': False, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2528018780.jpg', 'id': '27615441', 'cover_y': 2075, 'is_new': False}, {'rate': '7.2', 'cover_x': 1080, 'title': '一出好戏', 'url': 'https://movie.douban.com/subject/26985127/', 'playable': True, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2529571873.jpg', 'id': '26985127', 'cover_y': 1512, 'is_new': False}, {'rate': '8.0', 'cover_x': 527, 'title': '102岁不落伍', 'url': 'https://movie.douban.com/subject/30183666/', 'playable': False, 'cover': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2517839159.jpg', 'id': '30183666', 'cover_y': 764, 'is_new': True}, {'rate': '7.5', 'cover_x': 795, 'title': '真爱百分百', 'url': 'https://movie.douban.com/subject/30170375/', 'playable': False, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2516416600.jpg', 'id': '30170375', 'cover_y': 1080, 'is_new': True}, {'rate': '6.9', 'cover_x': 1383, 'title': '黑夜降临', 'url': 'https://movie.douban.com/subject/25864719/', 'playable': False, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535452413.jpg', 'id': '25864719', 'cover_y': 2048, 'is_new': True}, {'rate': '7.4', 'cover_x': 1968, 'title': '蚁人2：黄蜂女现身', 'url': 'https://movie.douban.com/subject/26636712/', 'playable': False, 'cover': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529389608.jpg', 'id': '26636712', 'cover_y': 2756, 'is_new': False}, {'rate': '7.3', 'cover_x': 2999, 'title': '动物世界', 'url': 'https://movie.douban.com/subject/26925317/', 'playable': True, 'cover': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2525528688.jpg', 'id': '26925317', 'cover_y': 4181, 'is_new': False}, {'rate': '6.9', 'cover_x': 5000, 'title': '快把我哥带走', 'url': 'https://movie.douban.com/subject/30122633/', 'playable': True, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2531080870.jpg', 'id': '30122633', 'cover_y': 7000, 'is_new': False}, {'rate': '7.7', 'cover_x': 1142, 'title': '江湖儿女', 'url': 'https://movie.douban.com/subject/26972258/', 'playable': False, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2533283770.jpg', 'id': '26972258', 'cover_y': 1600, 'is_new': False}, {'rate': '5.8', 'cover_x': 1000, 'title': '巨齿鲨', 'url': 'https://movie.douban.com/subject/26426194/', 'playable': True, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530572643.jpg', 'id': '26426194', 'cover_y': 1399, 'is_new': False}, {'rate': '8.2', 'cover_x': 2048, 'title': '碟中谍6：全面瓦解', 'url': 'https://movie.douban.com/subject/26336252/', 'playable': False, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2529365085.jpg', 'id': '26336252', 'cover_y': 3034, 'is_new': False}, {'rate': '6.9', 'cover_x': 2143, 'title': '镰仓物语', 'url': 'https://movie.douban.com/subject/26916229/', 'playable': True, 'cover': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2532008868.jpg', 'id': '26916229', 'cover_y': 2993, 'is_new': False}, {'rate': '7.9', 'cover_x': 694, 'title': '解除好友2：暗网', 'url': 'https://movie.douban.com/subject/26725678/', 'playable': False, 'cover': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2525020357.jpg', 'id': '26725678', 'cover_y': 1000, 'is_new': False}, {'rate': '8.3', 'cover_x': 690, 'title': '特工', 'url': 'https://movie.douban.com/subject/26683421/', 'playable': False, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2528281606.jpg', 'id': '26683421', 'cover_y': 986, 'is_new': False}, {'rate': '6.4', 'cover_x': 1371, 'title': '摩天营救', 'url': 'https://movie.douban.com/subject/26804147/', 'playable': True, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2527484082.jpg', 'id': '26804147', 'cover_y': 1920, 'is_new': False}, {'rate': '8.6', 'cover_x': 640, 'title': '幸福的拉扎罗', 'url': 'https://movie.douban.com/subject/27072795/', 'playable': False, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2521583093.jpg', 'id': '27072795', 'cover_y': 914, 'is_new': False}, {'rate': '5.2', 'cover_x': 679, 'title': '大师兄', 'url': 'https://movie.douban.com/subject/27201353/', 'playable': True, 'cover': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2528842218.jpg', 'id': '27201353', 'cover_y': 950, 'is_new': False}, {'rate': '6.9', 'cover_x': 1079, 'title': '风语咒', 'url': 'https://movie.douban.com/subject/30146756/', 'playable': True, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530872223.jpg', 'id': '30146756', 'cover_y': 1685, 'is_new': False}, {'rate': '6.2', 'cover_x': 2500, 'title': '狄仁杰之四大天王', 'url': 'https://movie.douban.com/subject/25882296/', 'playable': True, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2526405034.jpg', 'id': '25882296', 'cover_y': 3500, 'is_new': False}, {'rate': '6.8', 'cover_x': 1063, 'title': '精灵旅社3：疯狂假期', 'url': 'https://movie.douban.com/subject/26630714/', 'playable': False, 'cover': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530591543.jpg', 'id': '26630714', 'cover_y': 1488, 'is_new': False}]
# for list in lists:
#     print(type(list))
#     print(list['url'])
# # print(type(a),len(a))
# print(a)
import time
#
# lists = []
# if lists != []:
#     print(123)
# else:
#     print(456)
#
#
# start=int(time.time())
# print(start)

# t = time.time()
#
# nowTime = lambda:int(round(time.time() * 1000))
#
# print(nowTime())
# time.sleep(2)
# print(nowTime())

# d = {'a':1,'b':4,'c':2}
#
# a = sorted(d.items(),key = lambda x:x[1],reverse = True)
#
# for i in a:
#     print(i[0],i[1])

l = ['1','2','3']
m = ['4','5','6']

n = []

n.append(l)
n.append(m)
print(n)