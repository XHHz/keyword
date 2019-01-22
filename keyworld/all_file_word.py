# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/10/24 14:46
# @Author  : xhh
# @Desc    :
# @File    : all_file_word.py
# @Software: PyCharm
import sys
import os


#  获取文件的列表
def getfilelist(path):
    #path = 'file/text'
    listfile = []
    files = os.listdir(path)
    for f in files:
        if (f[0] == '.'):
            pass
        else:
            listfile.append(path)
            f = os.path.join("%s %s"%(path, f))
   # print(listfile, path)
    return listfile, path


# 读取一个文件夹下的文件
def getAllFile(filePath):
    fileDir = os.listdir(filePath)
    for allfiles in fileDir:
        allFileName = os.path.join("%s %s"%(filePath, allfiles))
        # print(allFileName)
        return allFileName





if __name__ == '__main__':
    (allfiles, path) = getfilelist()
    # for ff in path:
    #     print(allfiles)

    getAllFile('file/text')



