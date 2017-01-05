import string
def atoc(string):
    astring = string.strip()
    if astring[len(astring)-1] != 'j':
        return atof(astring)
    astring = astring[:len(astring)-1]
    index1 = astring.rfind('+')
    index2 = astring.rfind('-')
    if index1 < index2:
        i = astring[:index2]
        j = astring[index2+1:]
    else:
        i = astring[:index1]
        j = astring[index1+1:]

    return complex(float(i), float(j))


print atoc('1+2j')
print atoc('-1.23e+4-5.67j')
