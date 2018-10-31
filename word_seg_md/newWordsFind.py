# -*- coding:utf-8 -*-
"""
Chinese word segmentation algorithm without corpus.
Author:aluka.han
Email:aluka_hxl@gmail.com
Reference:
    https://github.com/Moonshile/ChineseWordSegmentation
    http://www.matrix67.com/blog/archives/5044
    https://zlc1994.com/2017/01/04/
"""
import math
import re
import sys
import time
from imp import reload

from globalVariable import fpath
from new_word_md.utils import file_name
from word_seg_md.createCandidateWords import gen_bigram, extract_cand_words
from word_seg_md.leftRightEntropy import cal_infor_entropy

reload(sys)

class GetWordInfo(object):
    """
    Store information of each word, including it's frequency, left neighbors and right neighbors
    """
    def __init__(self, text):
        """
        init function,the text is the word.
        :param text:the string will be compute,include fre,PMI,information entropy.
        """
        super(GetWordInfo, self).__init__()
        self.text = text
        self.freq = 0.0
        self.left = []
        self.right = []
        self.pmi = 0

    def update_att(self, left, right):
        """
        Increase frequency of this word, then append left/right neighbors.
        :param left: left neighbor set
        :param right: right neighbor set
        """
        self.freq += 1
        if left:
            self.left.append(left)
        if right:
            self.right.append(right)

    def compute_indexes(self, length):
        """
        Based on the update_att,compute tf and entropy of this word
        :param length: the length of document.
        """
        self.freq /= length
        self.left = cal_infor_entropy(self.left)
        self.right = cal_infor_entropy(self.right)

    def compute_info_entropy(self, words_dict):
        """
        compute the text's PMI, and select the min PMI for all bi-gram.
        :param words_dict: it's contain all candidate word information
        """
        sub_parts = gen_bigram(self.text)
        if len(sub_parts) > 0:
            self.pmi = min([math.log(
                    self.freq/(words_dict[leftg_rightg[0]].freq*words_dict[leftg_rightg[1]].freq)) for leftg_rightg in sub_parts])


class SegDocument(object):
    """
    Main class for Chinese word segmentation
    1. Generate words from a long enough document
    2. Do the segmentation work with the document
    """
    def __init__(self, doc, max_word_len=5, min_tf=0.000005, min_infor_ent=0.07, min_pmi=5):
        super(SegDocument, self).__init__()
        self.max_word_len = max_word_len
        self.min_tf = min_tf
        self.min_info_ent = min_infor_ent
        self.min_pmi = min_pmi
        self.word_infos = self.gen_words(doc)
        # calculate the average value for every index.
        word_count = float(len(self.word_infos))
        self.avg_len = sum([len(w.text) for w in self.word_infos]) / word_count
        self.avg_freq = sum([w.freq for w in self.word_infos]) / word_count
        self.avg_left_entropy = sum([w.left for w in self.word_infos]) / word_count
        self.avg_right_entropy = sum([w.right for w in self.word_infos]) / word_count
        self.avg_pmi = sum([w.pmi for w in self.word_infos]) / word_count
        self.avg_info_ent = sum([min(w.left, w.right) for w in self.word_infos]) / word_count
        # Filter out the results satisfy all the requirements
        filter_function = lambda v: len(v.text) > 1 and v.pmi > self.min_pmi and\
                    v.freq > self.min_tf and min(v.left, v.right) > self.min_info_ent
        self.word_tf_pmi_ent = [(w.text, w.freq, w.pmi, min(w.left, w.right)) for w in list(filter(filter_function, self.word_infos))]

    def gen_words(self, doc):
        """
        Generate all candidate words with their frequency/pmi/infor_entropy
        :param doc:the document used for words generation
        :return:
        """
        doc = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#”“￥：%……&*（）]+",
                      "", doc)
        suffix_indexes = extract_cand_words(doc, self.max_word_len)
        word_cands = {}
        # compute frequency and neighbors
        for suf in suffix_indexes:
            word = doc[suf[0]:suf[1]]
            if word not in word_cands:
                word_cands[word] = GetWordInfo(word)
            word_cands[word].update_att(doc[suf[0]-1:suf[0]], doc[suf[1]:suf[1]+1])

        # compute the tf and info_entropy
        doc_lens = len(doc)
        for word in word_cands:
            word_cands[word].compute_indexes(doc_lens)

        # compute PMI for every word, if len(word)>1
        values = sorted(list(word_cands.values()), key=lambda x: len(x.text))

        for v in values:
            if len(v.text) == 1:
                continue
            v.compute_info_entropy(word_cands)
        return sorted(values, key=lambda v: v.freq, reverse=True)
if __name__ == '__main__':

    files = file_name(fpath + '\\cawler_result')
    for file in files:
        start = time.clock()
        doc = open(fpath + '\\cawler_result\\' + file, 'r',encoding='utf-8').read()
        xx = SegDocument(doc)
        print((file + '平均长度:', xx.avg_len))
        print((file + '平均词频:', xx.avg_freq))
        print((file + '平均PMI:', xx.avg_pmi))
        print((file + '平均信息熵:', xx.avg_info_ent))
        data_wr = open(fpath + '\\word_seg_md\\result\\' + file.split(r'.')[0] + r'_result.txt', 'w', encoding='utf-8')
        for item in xx.word_tf_pmi_ent:
            # word.append([item[0], item[1], item[2], item[3]])
            data_wr.write(str(item[0])+','+str(item[1])+','+str(item[2])+','+str(item[3])+'\n')
        # df = pd.DataFrame(word, columns=['word', 'tf', 'pmi', 'info_ent'])
        # df.to_csv(path+'\\douban.csv', index=False)
        end = time.clock()
        print((end-start))
