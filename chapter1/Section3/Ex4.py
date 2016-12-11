import math
t = float(raw_input("Enter the tempeerature (Fahrenheit): "))
v = float(raw_input("Enter the velocity of wind (miles per hour): "))

if (math.sqrt(t) > 50 or v > 120 or v < 3):
    print "Invalid input"
else:
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*math.pow(v,0.16)
    print "The effective temperature of wind chill is: " + str(w)
