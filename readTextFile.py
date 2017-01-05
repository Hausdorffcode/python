'readTextFile.py -- read and display text file'

import os

#get filename
fname = os.getcwd() + '\\' + raw_input("Enter filename: ")
print

#attempt to open file for  reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open error: ", e
else:
    #display contents to the screen
    for eachline in fobj:
        print eachline.strip()
    fobj.close()
