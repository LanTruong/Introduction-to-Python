#kth root of n
import math
def k_Root(n,k):
    x0 = n
    EPSILON = 1e-10
    while abs(math.pow(x0,k)-n) > (EPSILON):
        # Replace t by the average of t and c/t.
        x0 = x0 - float(math.pow(x0,k)-n)/(k*math.pow(x0,k-1))
        print x0
    return x0
    


n = float(raw_input("Enter n: "))
k = int(raw_input("Enter k: "))
if (k%2 == 0):
    if (n<0):
        print "Invalid input."
    else:
        print k_Root(n,k)
else:
    print k_Root(n,k)

