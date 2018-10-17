# -*- coding:utf-8 -*-
"""
# @Author  : huxw
# @Update  : 2018/10/16 14:02
# @Software: PyCharm
"""

import time


def mergenews(type, n):
    list4art.artdict()
    list4e_sports.esportsdict()
    list4edu.edudict()
    # list4movie.moviedict()
    list4ent.entdict()
    list4health.healthdict()
    list4mil.mildict()
    list4money.moneydict()
    list4news.newsdict()
    list4sports.sportsdict()
    list4tech.techdict()
    list4travel.traveldict()
    # list4video.videodict()

    # 清空数据表操作
    mh = mysqlhelp.MysqlHelp()
    sql = "TRUNCATE TABLE show_newwords_newwords"
    mh.clearTable(sql=sql)

    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sql = "INSERT INTO show_newwords_runtime(time) VALUES('%s')" % (t)
    mh.insert(sql=sql)

    stopDic = getStopWords()

    # sort
    print ("\n############item:【教育】###############")
    top_edu = utils.sort(globallist.list_edu, n, type,'教育',stopDic)
    print ("\n############item:【娱乐】###############")
    top_fashion = utils.sort(globallist.list_ent, n, type,'娱乐',stopDic)
    print ("\n############item:【艺术】###############")
    top_car = utils.sort(globallist.list_art, n, type,'艺术',stopDic)
    print ("\n############item:【体育】###############")
    top_sport = utils.sort(globallist.list_sport, n, type,'体育',stopDic)
    # # print "\n############item:【电影】###############"
    # # top_ent = utils.sort(globallist.list_movie, n, type,stopDic)

    print ("\n############item:【健康】###############")
    top_health = utils.sort(globallist.list_health, n, type,'健康',stopDic)
    print ("\n############item:【军事】###############")
    top_mil = utils.sort(globallist.list_mil, n, type,'军事',stopDic  )
    print ("\n############item:【财经】###############")
    top_money = utils.sort(globallist.list_money, n, type,'财经',stopDic)
    print ("\n############item:【新闻】###############")
    top_news = utils.sort(globallist.list_news, n, type,'新闻',stopDic)
    print ("\n############item:【电竞】###############")
    top_esport = utils.sort(globallist.list_esports, n, type,'电竞',stopDic)
    print ("\n############item:【科技】###############")
    # globallist.f.writelines("\n############item:【科技】###############")
    top_tech = utils.sort(globallist.list_tech, n, type,'科技',stopDic)
    print ("\n############item:【旅游】###############")
    top_travel = utils.sort(globallist.list_travel, n, type,'旅游',stopDic)
    # print "\n############item:【视频】###############"
    # globallist.f.writelines("\n############item:【视频】###############")
    # top_video = utils.sort(globallist.list_video, n, type)



    # 新词累加的方法
    utils.total(utils.mergenewdict())





    # 生成dict进行管理
    # map_all.setdefault("toutiao", top_toutiao)
    # map_all.setdefault("yule", top_yule)
    # map_all.setdefault("video", top_video)
    # map_all.setdefault("tiyu", top_tiyu)
