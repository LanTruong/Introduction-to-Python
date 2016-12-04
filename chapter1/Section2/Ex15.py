#calculate the distance between a point (x,y) from the origin
import math
x = float(raw_input("Enter x: "))
y = float(raw_input("Enter y: "))

print "Distance (" + str(x) + "," + str(y) + ") is: " + str(math.sqrt(x**2 + y**2))
