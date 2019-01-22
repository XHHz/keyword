# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/22 15:46
# @Author  : xhh
# @Desc    :
# @File    : full_file_word.py
# @Software: PyCharm
import os
import numpy
import jieba
import jieba.posseg as pseg
import string
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import time

start = time.clock()

# 获取文件列表
def getfilelist():
    # path = "./input/"
    path = "file/text/"
    filelist = []
    files = os.listdir(path)
    # 返回指定文件夹包含的文件或文件夹的名字列表
    for f in files:
        if (f[0] == '.'):
            pass
        else:
            filelist.append(f)
    return filelist, path


# 对文档进行分词处理
def fenci(argv, path):
    # 保存分词结果的目录
    #sFilePath = './segfile'
    sFilePath = 'file/data/data1/'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)
    # 读取文档
    filename = argv  # 这里的argv是文档
    f = open(path + filename, 'r+', encoding="utf-8")
    file_list = f.read()
    f.close()

    # 对文档进行分词处理，采用默认模式
    seg_list = jieba.cut(file_list, cut_all=True)

    # 对空格，换行符进行处理
    result = []
    for seg in seg_list:
        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n"):
            result.append(seg)

    # 将分词后的结果用空格隔开，保存至本地。
    f = open(sFilePath + "/" + filename, "w+")
    f.write(' '.join(result))
    f.close()


# 读取已分词好的文档，进行TF-IDF计算
def Tfidf(filelist):
    #  filename = argv  # 这里的argv是文档
    # path = './segfile/'
    path = 'file/data/data3/'
    corpus = []  # 存取100份文档的分词结果

    # sFilePath = 'F:/fenciDoc/tfidffile'
    sFilePath = 'file/data/data4/'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)

    for ff in filelist:
        fname = path + ff
        #f = open(fname, 'r+')
        f = open(fname, 'r')
        print(fname)
        content = f.read()
        f.close()
        corpus.append(content)

    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    word = vectorizer.get_feature_names()  # 所有文本的关键字
    weight = tfidf.toarray()  # 对应的tfidf矩阵

    keyword = open(sFilePath + '/' + 'keyword.txt', 'w+')  # 保存关键词的文档
    # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
    for i in range(len(weight)):
        print(u"--------Writing all the tf-idf in the", i, u" file into ",
              sFilePath + '/' + str(i + 1) + '.txt', "--------")
        f = open(sFilePath + '/' + str(i + 1) + '.txt', 'w+')

        # 将每一篇的关键词存入
        keyword.write("第" + str(i + 1) + "篇关键词：" + '\n')
        x = weight[i]
        y = x.argsort()  # 返回从小到大的索引值
        max = len(word)
        # print(y)
        keyword.write(word[y[max - 1]] + "   " + str(x[y[max - 1]]) + "\n")
        keyword.write(word[y[max - 2]] + "   " + str(x[y[max - 2]]) + "\n")
        keyword.write(word[y[max - 3]] + "   " + str(x[y[max - 3]]) + "\n")
        keyword.write(word[y[max - 4]] + "   " + str(x[y[max - 4]]) + "\n")
        keyword.write("\n")

        f.write("全部分词和TFIDF值：" + "\n")
        for j in range(len(word)):
            f.write(word[j] + "    " + str(weight[i][j]) + "\n")
        f.close()


if __name__ == "__main__":
    (allfile, path) = getfilelist()
    for ff in allfile:
        print("Using jieba on " + ff)
        fenci(ff, path)

    Tfidf(allfile)
    end = time.clock()
    print("运行时间" + str(end - start) + "秒")
