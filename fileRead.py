# -*- coding: cp936 -*-
try:
    filename = raw_input("Enter your file name: ")
    fobj = open(filename, "r")
    for eachline in fobj:
        print eachline, #ÿ���ı��Ѿ��Դ��˻��з�
    fobj.close()
except IOError, e:
    print "file open error: ", e
