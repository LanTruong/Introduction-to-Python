import random
x = 2.0
y = 2.0

while (x**2 + y**2 >1):
    x = -1.0 + 2.0*random.random()
    y = -1.0 + 2.0*random.random()

print x,y
