##prompt argument and verify sin^2 + cos^2 =1
import math
theta = float(raw_input("input an argument: "))
if math.fabs((math.sin(theta)**2 + math.cos(theta)**2 - 1.0)) < math.exp(-20):
    print "sin^2 + cos^2 = 1 is right"
else:
    print "sin^2 + cos^2 = 1 is false" 
