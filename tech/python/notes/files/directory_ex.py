# -*- coding: utf-8 -*-

import os

# 1. 获取当前的目录名称。
def getCurrentDirectory():
    return os.getcwd()

# lianbche d:\Learning\git\knowledge-map\tech\python\notes\files
# > python directory_ex.py
# d:\Learning\git\knowledge-map\tech\python\notes\files

# 2. 获取目录下的所有文件及文件夹。
def getAllFilesInDirectory(dir):
    return os.listdir(dir)

# lianbche d:\Learning\git\knowledge-map\tech\python\notes\files
# > python directory_ex.py
# ['directory_ex.py', 'file_ex.py']


print getAllFilesInDirectory(getCurrentDirectory())
