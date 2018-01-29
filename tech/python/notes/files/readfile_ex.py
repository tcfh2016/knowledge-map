# -*- coding: utf-8 -*-

def print_file(name):
    f = open(name, 'r')
    for line in f:
        print line,
    f.close()

# 由于print函数会在每行的内容默认附加'\n'，所以在使用 print (line)，输出如下：
# > python readfile_ex.py
# this is a Test
#
# right here.
#
# who you are.
#因此，如果不想要多余的空行，那么使用 print (line, end='')，但是这种用法只在Python3.x
#当中有效，下面链接有好几种方案，最简单的是 "print line,"
#
# https://www.reddit.com/r/learnpython/comments/3o4f9k/python_3_feature_into_python_27_end/

print_file("test.txt")
