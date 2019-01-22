# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/19 15:38
# @Author  : xhh
# @Desc    :ieba分词与wordcloud提取词云
# @File    :text_wordcloud.py
# @Software: PyCharm

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


with open('file/text/gangwei.txt', 'r', encoding='utf-8') as f:
    text = f.read()
with open('file/text/sample.txt', 'r',  encoding='utf-8') as f:
    tingyongci = f.read()

path = 'image/aaa.png'
font = 'font/youyuan.TTF'

text = text.replace('，','')
text = text.replace('1','')
text = text.replace('、','')
text = text.replace('；','')
text = text.replace('.','')
text = text.replace('。','')
text = text.replace('\\xa0', ' ')
str_list = jieba.cut(text) #使用精准模式来分词

'''加载停用词表并去掉停用词'''
outstr = ''
for word in str_list:
    if word not in tingyongci:
        if word != '\t':
            outstr += word
            outstr += ' '
img = Image.open(path)  # 打开图片
img_array = np.array(img)  # 将图片转换为数组3.3

wc = WordCloud(
    background_color='white',
    width=1000,
    height=800,
    mask=img_array,
    font_path=font
)
# print(outstr)
wc.generate_from_text(outstr)  # 绘制图片
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.figure()
plt.show()
wc.to_file('image/bbb.png')

