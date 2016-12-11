#solve quadratic equation
import math
a = int(raw_input("Enter a: "))
b = int(raw_input("Enter b: "))
c = int(raw_input("Enter c: "))

if (a == 0):
    print "The equation is not quadratic equation"
    print "One solution is :" + str((float)(-b)/c)
else: 
    delta = b**2 - 4*a*c
    if (delta == 0):
        print "this equation have only one solution: " + str((float)(-b)/(2*a))
    else:
        x1 = (float)(-b + math.sqrt(delta))/(2*a)
        x2 = (float)(-b - math.sqrt(delta))/(2*a)
        print "This equation has two solution: " + str(x1) + " " + str(x2)
