# -*- coding: utf-8 -*-
"""
# @Time    : 2018/05/26 下午5:13
# @Update  : 2018/09/28 上午10:30
# @Author  : zhanzecheng/片刻
# @File    : demo.py.py
# @Software: PyCharm
"""
import os
import jieba

from tokenizer.config import basedir
from tokenizer.model import TrieNode
from tokenizer.utils import get_stopwords, load_model, load_dictionary, save_model, generate_ngram, file_name


def load_data(filename, stopwords):
    """
    :param filename:
    :param stopwords:
    :return: 二维数组,[[句子1分词list], [句子2分词list],...,[句子n分词list]]
    """
    data = []
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            word_list = [x for x in jieba.cut(line.strip(), cut_all=False) if x not in stopwords]
            data.append(word_list)
    return data


def load_data_2_root(data):
    print('------> 插入节点')
    for word_list in data:
        # tmp 表示每一行自由组合后的结果（n gram）
        # tmp: [['它'], ['是'], ['小'], ['狗'], ['它', '是'], ['是', '小'], ['小', '狗'], ['它', '是', '小'], ['是', '小', '狗']]
        ngrams = generate_ngram(word_list, 3)
        for d in ngrams:
            root.add(d)
    print('------> 插入成功')


if __name__ == "__main__":
    root_name = basedir + "/data/root.pkl"
    stopwords = get_stopwords()
    if os.path.exists(root_name):
        root = load_model(root_name)
    else:
        dict_name = basedir + '/data/dict.txt'
        word_freq = load_dictionary(dict_name)
        root = TrieNode('*', word_freq)
        save_model(root, root_name)

    # 加载新的文章
    fpath = os.path.abspath(os.path.join(os.getcwd(), "..")) + '\\result\\'
    files = file_name(fpath)
    for file in files:
        data = load_data(fpath+file, stopwords)
        # 将新的文章插入到Root中
        load_data_2_root(data)
        # 定义取TOP5个
        topN = 40
        result, add_word = root.find_word(topN)
        # 如果想要调试和选择其他的阈值，可以print result来调整
        # print("\n----\n", result)
        fc_file = open(fpath+file.split(r'.')[0]+r'_fenciresult.txt','a',encoding='utf-8')
        print("\n----\n", '增加了 %d 个新词, 词语和得分分别为: \n' % len(add_word))
        fc_file.write("\n----\n"+'增加了 %d 个新词, 词语和得分分别为: \n' % len(add_word))
        print('#############################')
        for word, score in add_word.items():
            print(word + ' ---->  ', score)
            fc_file.write(word + ' ---->  ' + str(score ) + '\n')
        print('#############################')
        fc_file.close()


    # data = load_data(basedir+'\data\demo.txt', stopwords)
    # # 将新的文章插入到Root中
    # load_data_2_root(data)
    # # 定义取TOP5个
    # topN = 20
    # result, add_word = root.find_word(topN)
    # # 如果想要调试和选择其他的阈值，可以print result来调整
    # # print("\n----\n", result)
    # print("\n----\n", '增加了 %d 个新词, 词语和得分分别为: \n' % len(add_word))
    # for word, score in add_word.items():
    #     print(word + ' ---->  ', score)

    # 前后效果对比
    # test_sentence = '蔡英文在昨天应民进党当局的邀请，准备和陈时中一道前往世界卫生大会，和谈有关九二共识问题'
    # print('添加前：')
    # print("".join([(x + '/ ') for x in jieba.cut(test_sentence, cut_all=False) if x not in stopwords]))
    #
    # for word in add_word.keys():
    #     jieba.add_word(word)
    # print("添加后：")
    # print("".join([(x + '/ ') for x in jieba.cut(test_sentence, cut_all=False) if x not in stopwords]))