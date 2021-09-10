# -*- coding: utf-8 -*-

import os

# 1. 获取当前的目录名称。
def getCurrentDirectory():
    return os.getcwd()

# lianbche d:\Learning\git\knowledge-map\tech\python\notes\files
# > python directory_ex.py
# d:\Learning\git\knowledge-map\tech\python\notes\files

# 2. 获取目录下的所有文件及文件夹。
def getAllFileAndDirInDirectory(dir):
    return os.listdir(dir)

# lianbche d:\Learning\git\knowledge-map\tech\python\notes\files
# > python directory_ex.py
# ['directory_ex.py', 'file_ex.py']

# 3. 获取目录下的所有的文件。使用Python 语言中的 List Comprehensions。
# http://www.secnetix.de/olli/Python/list_comprehensions.hawk
def getAllFilesInDirectory(dir):
    return [f for f in getAllFileAndDirInDirectory(dir)  if os.path.isfile(f)]
# 测试输出：
# lianbche d:\Learning\git\knowledge-map\tech\python\notes\files
# > python directory_ex.py
# ['directory_ex.py', 'file_ex.py']

# 4. 获取目录下的所有的文件夹。使用Python 语言中的 List Comprehensions。
def getAllDirsInDirectory(dir):
    return [d for d in getAllFileAndDirInDirectory(dir)  if os.path.isdir(d)]
# 测试输出：
# lianbche d:\Learning\git\knowledge-map\tech\python\notes\files
# > python directory_ex.py
# []

# 5. 统计目录下的所有的文件的大小，不统计目录。
def countFileSizeInDirectory(dir):
    total = 0;
    for f in getAllFileAndDirInDirectory(dir):
        total += os.stat(f).st_size
    return total
# 测试输出：
# lianbche d:\Learning\git\knowledge-map\tech\python\notes\files
# > python directory_ex.py
# 1632

print countFileSizeInDirectory(getCurrentDirectory())
