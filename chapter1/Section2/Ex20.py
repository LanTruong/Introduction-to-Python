#take two inputs of day and month and check whether they are between March 20 and June 20
#suppose valid input

d = int(raw_input("Enter the day: "))

m = int(raw_input("Enter the month: "))
m1 = 3
m2 = 6

if (m1 < m and m < m2 ):
    print "True"
elif (m1 == m):
    if (d >= 20):
        print "True"
    else:
        print "False"
elif (m == m2):
    if (d <= 20):
        print "True"
    else:
        print "False"
else:
    print "False"
