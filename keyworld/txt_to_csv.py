# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/19 15:38
# @Author  : xhh
# @Desc    :
# @File    : txt_to_csv.py
# @Software: PyCharm
import numpy as np
import pandas as pd

from jieba.analyse import *
with open('file/text/gangwei.txt', encoding='utf-8') as f:
    data = f.read()

# 利用textrank提取关键字
for keyword, weight in textrank(data, withWeight=True):
    print('%s  %s' % (keyword, weight))

