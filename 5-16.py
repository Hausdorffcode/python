def payment(init, paid):
    count = 0
    print "Pymt#   Paid      Banalce"
    print "-----   ----      -------"
    print "%d       $%.2f    $%.2f" %(count, paid, init)
    while init > 0:
        count += 1
        if init > paid:
            init -= paid
        else:
            paid = init
            init = 0
        print "%d       $%.2f    $%.2f" %(count, paid, init)


init = float(raw_input("Enter opening balance: "))
paid = float(raw_input("Enter monthly payment: "))
payment(init, paid)
