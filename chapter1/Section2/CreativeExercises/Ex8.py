#Mercator projection
#
import math
lambda0 = float(raw_input("Enter longitude of the center of the map: "))
lamda = float(raw_input("Enter longitude of the point: "))
phi = float(raw_input("Enter latitude of the point: "))

x = 0.5*(math.log((1+math.sin(phi))/(1-math.sin(phi))))
y = float((lamda - x))/lambda0

print "x:= " + str(x) + " , y:= " + str(y)
