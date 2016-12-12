#compute the euclidean distance of two vectors
import math
def Euclidean(a,b):
    if len(a) == len(b):
        s = 0.0 
        for i in range(0,len(a)):
            s += (a[i] - b[i])**2
        return math.sqrt(s)
    else:
        print "Error. Two Vector are not alligned"
    
a = [1,2,3]
b = [2,3,4]
print Euclidean(a,b)
