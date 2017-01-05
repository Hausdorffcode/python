
mylist = []

def input_list_data():
    input_list_length = -1
    while(not (0 < int(input_list_length) < 11)):
        input_list_length = raw_input("please enter the number of numbers your want to calculate, it should be in range 1 to 10: ")
    while(len(mylist) < int(input_list_length)):
        input_list_number = raw_input("please enter the number you want to calculate, it should be in range 1 to 100 :")
        if not (0 < int(input_list_number) < 101):
            print "Invalid, please enter again"
            return
        mylist.append(int(input_list_number))
        #print mylist

def list_sum(alist):
    mysum = 0
    for item in alist:
        mysum += item
    return mysum

def list_average(alist):
        return float(list_sum(alist)) / len(alist)

def start_choose():
    print "1 calulate the sum"
    print "2 calulate the average"
    print "X exit"
    choose = raw_input("please enter your choose: ")
    if(choose == '1'):
        print "the sum is " + str(list_sum(mylist))
    elif(choose == '2'):
        print "the average is " + str(list_average(mylist))
    elif(choose == 'x'):
        return
    else:
        print "Invalid input"
        start_choose()

input_list_data()
start_choose()
