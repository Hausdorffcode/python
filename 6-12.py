def findchr(string, char):
    index = 0
    for item in string:
        if char == item:
            break
        index += 1
    return (index if index < len(string) else -1)

print findchr('adfggdcv234', 'g')
print findchr('fd', 'g')

def rfindchr(string, char):
    for i in reversed(range(len(string))):
        #print i
        if char == string[i]:
            return i
    return -1

print rfindchr('fdfefghgsdgwAQ', 'g')
print rfindchr('fgdf', 't')


def subchr(string, origchar, newchar):
    pass
