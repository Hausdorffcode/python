import time
import hashlib

db = {}
#in db, the item is {name.lower() : [password, time]}

def checkName(name):
    if ' ' in name:
        return False
    return True

def newuser(name):
    pwd = raw_input('passwd: ')
    localtime = time.time()
    db[name] = [pwd, localtime]    

def olduser(name):
    pwd = raw_input('passwd: ')
    passwd = db.get(name)[0]
    if passwd == pwd:
        print 'welcome back', name
        localtime = time.time()
        if localtime-(4*3600) <= db[name][1] :
            print 'You already logged in at: %s' %time.ctime(localtime)
        db[name][1] = localtime
    else:
        print 'login incorrect'

def userLogin():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt).lower()
        if not checkName(name):
            prompt = 'invalid name, please try again: '
            continue
        else:
            break
    if name not in db:
        isNewUser = raw_input("Is new user?\n(Y)es\n(N)o\n")
        if isNewUser.lower()=='y': newuser(name)
    else:
        olduser(name)

def delete():
    username = raw_input('Enter the user to delete: ').lower()
    if username not in db:
        print "don't have the user"
    else:
        del db[username]
        print "Done %s have been removed" % username

def display():
    print "user      password"
    print "----      --------"
    for item in db.items():
        print "%s%10s" % (item[0], item[1][0])

def manage():
    prompt = '''
(D)elete a user
dis(P)lay all users
(B)ack
Enter choice: '''
    done = False
    while not done:
        chosen = False
        while not chosen:
            choice = raw_input(prompt).strip()[0].lower()
            print '\nYou picked: [%s]' % choice
            if choice not in 'dpb':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'd': delete()
        if choice == 'p': display()
        if choice == 'b': done = True
       
def showmenu():
    prompt = '''
(U)ser Login
(M)anage
(Q)uit
Enter choice: '''

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'uqm':
                print 'invalid option, try again'
            else:
                chosen = True

        if choice == 'q': done = True
        if choice == 'u': userLogin()
        if choice == 'm': manage()

if __name__ == '__main__':
    showmenu()
