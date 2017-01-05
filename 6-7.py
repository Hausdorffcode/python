

num_str = raw_input('Enter a number: ')
num_num = int(num_str)
fac_list = range(1, num_num+1)
print "BEFORE:", fac_list

i = 0
another_list = []
fac_list_length = len(fac_list)
while i < fac_list_length:
    if num_num % fac_list[i] != 0:
        another_list.append(fac_list[i])
    i += 1
fac_list = another_list
print "AFTER:", fac_list
