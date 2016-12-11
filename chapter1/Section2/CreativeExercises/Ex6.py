#Day of week
#get 3 inputs from commandline then write the day of week on which that date falls

m = int(raw_input("Enter month: "))
d = int(raw_input("Enter day: "))
y = int(raw_input("Enter year: "))

y0 = y - (14 - m)/12
x = y0 + y0/4 -y0/100 + y0/400
m0 = m + 12*((14-m)/12)-2
d0 = (d+x+(31*m0)/12) % 7

if (d0 == 0):
    print "Sunday"
elif (d0 == 1):
    print "Monday"
elif (d0 == 2):
    print "Tuesday"
elif (d0 == 3):
    print "Wednesday"
elif (d0 == 4):
    print "Thursday"
elif (d0 == 5):
    print "Friday"
elif (d0 == 6):
    print "Saturday"
