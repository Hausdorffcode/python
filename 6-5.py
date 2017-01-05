def mycmp(str1, str2):
    if len(str1) != len(str2):
        return False
    isequ = True
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            isequ = False
            break
    return isequ

print mycmp('abc', 'abc')
print mycmp('123', 'ghr')
print mycmp('dec', 'Dec')

def huiwen(astring):
    reverseList = list(astring)
    reverseList.reverse()
    #print reverseList
    return astring + ''.join(reverseList)

print huiwen('123')
print huiwen('12hghg  sdf')
