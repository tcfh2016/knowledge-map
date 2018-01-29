# -*- coding: utf-8 -*-

def write_file(name):
    f = open(name, 'w')
    f.write("You and me ")
    f.write("learn python together.")

    f.close()

write_file("test.txt")
