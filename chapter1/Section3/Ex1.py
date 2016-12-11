#take three integer input and check whether 'equal' or 'not-equal'
a1 = int(raw_input("Enter first integer: "))
a2 = int(raw_input("Enter second integer: "))
a3 = int(raw_input("Enter third integer: "))

if (a1 == a2 and a2 == a3):
    print "equal"
else:
    print "not equal"
