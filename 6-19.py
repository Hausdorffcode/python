# -*- coding: cp936 -*-
def display(container, num, horv):
    alist = list(container)
    alist_len = len(alist)
    per = alist_len / num
    if horv:
        for i in range(alist_len - per):
            count = i%per
            if count == per-1:
                print '%s' % str(i)
            else:
                print '%s' % str(i),
        for i in range(alist_len - per, alist_len):
            print '%s' % str(i),
    #按列显示


a = [x for x in range(100)]
display(a, 7, True)
