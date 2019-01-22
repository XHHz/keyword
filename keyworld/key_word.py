# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/22 15:27
# @Author  : xhh
# @Desc    :
# @File    : key_word.py
# @Software: PyCharm
from jieba.analyse import *

fileName = "file/text/gangwei.txt"
outFile = "file/text/gangwei_out.csv"
outFile1 = "file/text/gangwei_out1.txt"
# 打开文件
with open(fileName, encoding='utf-8') as f:
    data = f.read()
    data = data.replace('\\xa0', ' ')

# 利用extract_tags提取关键字
list_test = []
# 提取权重， 并将所提取的关键字以列表的形式存到列表中去
for keyword, weight in textrank(data,  withWeight=True):
    list_test.append([keyword, weight])
# 按列表写入到文件中
with open(outFile, 'w', encoding='utf-8') as m:
    for i in list_test:
       m.write(str(i).replace('[', '').replace(']', ''))
       m.write('\n')

# 利用textrank提取关键字
# for keyword, weight in extract_tags(data, topK=10, withWeight=True):
#     print('%s  %s' % (keyword, weight)) b