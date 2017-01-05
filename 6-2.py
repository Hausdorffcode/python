import string
import keyword

alphas = string.letters + '-'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput  = raw_input('Identifier to test?')

if len(myInput) >= 1:
    if myInput[0] not in alphas:
        print '''invalid: first symbol must be
            alphabetic'''
    elif len(myInput) == 1:
        print 'okey as a indentifier'
    elif keyword.iskeyword(myInput):
        print '''invalid: the word is keyword'''
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print '''invalid: remmaining
                    symbols must be alphanumeric'''
                break
        else:
            print 'okey as a indentifier'
else:
    print 'please enter something!'
