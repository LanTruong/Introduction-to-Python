import random
import math
x = 2.0
y = 2.0

while (x**2 + y**2 >=1):
    x = -1.0 + 2.0*random.random()
    y = -1.0 + 2.0*random.random()

a = 2*x*math.sqrt(1-x**2-y**2)
b = 2*y*math.sqrt(1-x**2-y**2)
c = 1 - 2*(x**2+y**2)
print a,b,c
print str(a**2 + b**2 + c**2)
