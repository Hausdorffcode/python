import types

def getIntBitSize():
    i = 1
    size = 1
    while type(i) is types.IntType:
        i <<= 1
        size += 1
    return size

print getIntBitSize()

def getLongBitSize():
    i = 1L
    size = 1
    while type(i) is types.LongType:
        i <<= 1
        size += 1
    return size

#print getLongBitSize()

