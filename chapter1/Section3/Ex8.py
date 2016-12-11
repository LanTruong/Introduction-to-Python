#uniform random numbers
import random
n = int(raw_input("Enter a number: "))
u = []
for i in range(0,n):
    u.append(random.random())
print "average: " + str(float(sum(u))/len(u))
print "max: " + str(max(u))
print "min: " + str(min(u))
