"this is a calculator"

def cal(a, b, op):
    a1 = float(a)
    b1 = float(b)
    if op == '+':
        return a1+b1
    if op == '-':
        return a1-b1
    if op == '*':
        return a1*b1
    if op == '/':
        return a1/b1
    if op == '%':
        return a1%b1
    if op == '**':
        return a1**b1

def stringToList(astring):
    return astring.split()

def calculator():
    usrInput  = raw_input("Enter your expresson: ")
    alist = stringToList(usrInput)
    print alist
    return cal(alist[0], alist[2], alist[1])

print calculator()
#the input must have whitespace between number and opertor
