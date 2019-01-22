# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/22 10:23
# @Author  : xhh
# @Desc    :
# @File    : text_keyWorld.py
# @Software: PyCharm
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# 打开文件
filename = 'file/text/gangwei.txt'
with open(filename, encoding='utf-8') as f:
    text1 = f.read()
    text1 = text1.replace('\\xa0', ' ')
    # print(text1)

mytext = ' '.join(jieba.cut(text1))
# print(mytext)

word_cloud = WordCloud(font_path="font/simsun.ttf").generate(mytext)
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.show()
word_cloud.to_file('image/key_word.png')




