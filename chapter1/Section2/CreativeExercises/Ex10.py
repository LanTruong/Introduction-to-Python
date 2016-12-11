#Great Circle
import math
x1 = float(raw_input("Enter latitude (in degrees) of first point: "))
y1 = float(raw_input("Enter longitude (in degrees) of first point: "))
x2 = float(raw_input("Enter latitude (in degrees) of second point: "))
y2 = float(raw_input("Enter longitude (in degrees) of second point: "))

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

d = math.acos(math.sin(x1)*math.sin(x2) + math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print "Distance with assumption perfect circle: " + str(60*math.degrees(d))

a = (math.sin((x1-x2)/2))**2 + math.cos(x1)*math.cos(x2)*(math.sin((y1-y2)/2))**2
c = 2*math.asin(min(1,math.sqrt(a)))
print "Distance according to Haversine Formula: " + str(60*math.degrees(c))

p1 = math.cos(x2)*(math.sin(y1-y2))**2
p2 = (math.cos(x1)*math.sin(x2)-math.sin(x1)*math.cos(x2)*math.cos(y1-y2))
p3 = math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2)

delta = math.atan((math.sqrt(p1**2+p2**2))/(p3))
print "Distance with accurate for all distances: " + str(60*math.degrees(delta))

