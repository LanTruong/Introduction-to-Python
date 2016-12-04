##Gaussian random numbers
import random
import math
u = random.random()
v = random.random()
Z = math.sin(math.pi * 2 * v) * (-2 * math.log(u))**0.5

print "Z: = " + str(Z)
