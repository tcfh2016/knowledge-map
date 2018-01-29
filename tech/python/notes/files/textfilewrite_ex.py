# -*- coding: utf-8 -*-

def write_file(name):
    f = open(name, 'w')
    f.write("You and me ")
    f.write("learn python together.")

    f.close()


# 如上是一个写文件的例子，下面是一个在文件头插入内容的例子。

def insert_title(title, fname='textfilereadtest.txt'):
    f = open(fname, 'r+')
    content = f.read()
    content = title + "\n\n" + content
    f.seek(0)
    f.write(content)
    f.close()

insert_title("Our Story", "textfilereadtest.txt")
