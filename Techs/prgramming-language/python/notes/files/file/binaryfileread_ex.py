# -*- coding: utf-8 -*-

def is_gif(fname):
    f = open(fname, 'br')
    first4byte = tuple(f.read(4))
    return first4byte == (0x47, 0x49, 0x46, 0x38)

# 如上函数是通过读取一个文件前面4个字节来判断是否为gif格式的文件。
