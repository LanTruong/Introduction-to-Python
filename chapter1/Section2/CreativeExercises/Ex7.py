#uniform random numbers
#write 5 random numbers in range [0,1). their average, minimum and maximum
import random
import math

def mean(a):
    return float(sum(a))/len(a)

a = []
a.append(random.random())
a.append(random.random())
a.append(random.random())
a.append(random.random())
a.append(random.random())

print "list of 5 numbers: " + str(a)
print "maximum of a: " + str(max(a))
print "mean of a: "+ str(mean(a))
print "minimum of a: "+ str(min(a))



