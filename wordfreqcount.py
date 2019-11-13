#! python3
# -*- coding: utf-8 -*-
import os, codecs
import jieba
from collections import Counter

ROOT_PATH = "/home/vagrant/PycharmProjects/Collection2/autohome/"


def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果')
    k_list = []
    for (k, v) in c.most_common(5000):
        k_list.append(k)
        print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * 5, v))

    return k_list


def unitfile():
    filename_list = ['content_advice.txt', 'content_drive.txt', 'content_tech.txt']
    f = open("other_data_file/content_adv_dri_tech.txt", "w")
    f.close()
    count = 0
    for item in filename_list:
        f = open(ROOT_PATH + "auto_clean_sentence_txt/" + item, "r")
        lines = f.readlines()
        count += len(lines)
        f_totle = open("other_data_file/content_adv_dri_tech.txt", "w")
        for line in lines:
            f_totle.write(str(line))
        print(count)
        f_totle.close()


def main():
    # unitfile()
    # new_file_path = ROOT_PATH + "auto_clean_sentence_txt/content_adv_dri_tech.txt"
    new_file_path = "split_data.txt"
    # high_freq_word = ROOT_PATH + "auto_clean_sentence_txt/adv_dri_tech_high_freq_word_2.txt"
    high_freq_word = "zhangyan_data/freq_word_zhangyan.txt"
    with codecs.open(new_file_path, 'r', 'utf8') as f:
        txt = f.read()
    with codecs.open(high_freq_word, 'w', 'utf8') as f_w:
        words = get_words(txt)
        for word in words:
            f_w.write(word + '\n')
    f.close()
    f_w.close()


if __name__ == '__main__':
    main()
