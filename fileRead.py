# -*- coding: cp936 -*-
try:
    filename = raw_input("Enter your file name: ")
    fobj = open(filename, "r")
    for eachline in fobj:
        print eachline, #每行文本已经自带了换行符
    fobj.close()
except IOError, e:
    print "file open error: ", e
