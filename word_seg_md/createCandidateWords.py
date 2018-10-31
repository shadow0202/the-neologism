# -*- coding:utf-8 -*-
"""
Algorithms about extract candidate words from document.
Author:aluka.han
Email:aluka_hxl@gmail.com
Reference:
    https://github.com/Moonshile/ChineseWordSegmentation
    http://www.matrix67.com/blog/archives/5044
    https://zlc1994.com/2017/01/04/
"""
import os
import re
import sys
from imp import reload



def extract_cand_words(_doc, _max_word_lens):
    """
    Treat a suffix as an index where the suffix begins.
    Then sort these indexes by the suffixes.
    :param _doc: the document need segment.
    :param _max_word_lens: the max length of candidate word.
    :return: the candidate words index in document.
    """
    indexes = []
    doc_len = len(_doc)
    for i in range(doc_len):
        for j in range(i + 1, min(i + 1 + _max_word_lens, doc_len + 1)):
            indexes.append((i, j))
    return sorted(indexes, key=lambda i_j: _doc[i_j[0]:i_j[1]])


def gen_bigram(_word_str):
    """
    Partition a string into all possible two parts, e.g.
    given "abcd", generate [("a", "bcd"), ("ab", "cd"), ("abc", "d")]
    For string of length 1, return empty list,n-gram can split n1-gram and n2-gram,and n1+n2 = n.
    if a word length is n and n-1 different kinds of split.
    :param _word_str:
    :return:
    """
    return [(_word_str[0:_i], _word_str[_i:]) for _i in range(1, len(_word_str))]

