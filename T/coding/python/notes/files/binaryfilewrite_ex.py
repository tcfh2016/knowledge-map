# -*- coding: utf-8 -*-

import pickle

def make_picked_file():
    grades = {'alan' : [4, 8, 10, 10],
              'tom'  : [7, 7, 7,  8]}

    ofile = open('binaryfiletest.bin', 'wb')
    pickle.dump(grades, ofile)

def get_picked_data():
    ifile = open('binaryfiletest.bin', 'rb')
    grades = pickle.load(ifile)
    ifile.close()
    return grades

make_picked_file()
print (get_picked_data())
