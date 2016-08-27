# -*- coding: utf-8 -*-

import jieba
import logging

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # jieba custom setting.
    jieba.set_dictionary('jieba_dict/dict.txt.big')

    # load stopwords set
    stopwords =open('jieba_dict/stopwords.txt','r').read()
    stopwordset = set(stopwords)
    texts_num = 0

    output = open('wiki_seg.txt','w')
    with open('wiki_zh_tw.txt','r') as content :
        for line in content:
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopwordset:
                    output.write(word +' ')

            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("已處理 %d 個 token" % texts_num)
    output.close()

if __name__ == '__main__':
    main()