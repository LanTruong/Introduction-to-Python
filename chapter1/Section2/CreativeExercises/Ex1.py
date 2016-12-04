##Continuously compounded interest
import math
P = float(raw_input("Enter the principal: "))
r = float(raw_input("Enter the interest rate: "))
t = float(raw_input("Enter the number of year: "))


print "After " + str(t) + " years, you will get " + str(P*math.exp(r*t))
