#functiongrowth
import math
print "log n" + "\t\t" + "n" + "\t" + "n log n       " + "\t" + "n**2"
for i in range(1,12):
    print str(math.log(2**i)) + "\t" + str(2**i)+ "\t"+ str(2**i*math.log(2**i)) + "\t" + str(2**(2*i))
