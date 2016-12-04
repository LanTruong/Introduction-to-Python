#calculate the position of an object after t seconds with initial position x0 and velocity v0
x0 = float(raw_input("Enter the initial position: "))
v0 = float(raw_input("Enter the initial velocity: "))
t = float(raw_input("Enter second: "))
G = 9.80685

x = x0 + v0*t - G*t**2/2
print "Distance from initial position after " + str(t) + " seconds: " + str(x)
