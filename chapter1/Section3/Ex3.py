##check whether two float is strictly in range (0,1)
x1 = float(raw_input("Enter the first number: "))
x2 = float(raw_input("Enter the second number: "))

if (0 < x1 and x1 > 0 and x2 > 0 and x2 <1):
    print "True"
else:
    print "False"
