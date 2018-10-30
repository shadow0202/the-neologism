# -*- coding: utf-8 -*-
"""
# @Author  : huxw 
# @Update  : 2018/10/30 15:56 
# @Software: PyCharm
"""
import jieba
import jieba.posseg

from globalVariable import list_cixing, fpath
from new_word_md.utils import file_name, get_stopwords


# 读取爬取结果
def readres(path):
    res = open(path,'r',encoding='utf-8')
    res_txt = res.read()
    return res_txt


# 结巴分词
# 去掉部分词性
def fenci(path):
    data= []
    res_txt = readres(path)
    stopwords = get_stopwords()
    word_list = [x for x in jieba.cut(res_txt.strip(), cut_all=False) if x not in stopwords]
    for word in word_list:
        poss = jieba.posseg.cut(word)
        for u in poss:
            if u.flag not in list_cixing:
                data.append(u.word)
    return data


# 纪录单词频率
def record(l):
    list_record = []
    list_set = set(l)
    for item in list_set:
        # print("the %s has found %d" % (item, l.count(item)))
        list_record.append(item + '\t' + str(l.count(item)))
    return list_record


if __name__ == '__main__':
    files = file_name(fpath+'\\cawler_result')
    print('——————正在结巴分词————————')
    for file in files:
        data = fenci(fpath + '\\cawler_result\\' + file)
        data_wr = open(fpath + '\\jieba_md\\result\\' + file.split(r'.')[0] + r'_result.txt','w',encoding='utf-8')
        record_res = record(data)
        for res in record_res:
            data_wr.write(res + '\n')
    print('————————success————————')