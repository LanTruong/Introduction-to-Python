##Polar coordinates
import math
x = float(raw_input("Enter x: "))
y = float(raw_input("Enter y: "))

r = math.sqrt(x**2 + y**2)
theta = math.atan2(y,x)/math.pi
print "r: =" +str(r) + " and theta: = " + str(theta) + "pi" 
