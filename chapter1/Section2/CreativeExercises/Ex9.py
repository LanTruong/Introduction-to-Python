#Color conversion
r = float(raw_input("Enter R: "))
g = float(raw_input("Enter G: "))
b = float(raw_input("Enter B: "))

if (r == 0 and g ==0 and b ==0 ):
    print "C = 0, M = 0, Y = 0 and K = 1"
else:
    W = max(r/255,g/255,b/255)
    C = (W - r/255)/W
    M = (W - g/255)/W
    Y = (W - b/255)/W 
    K = 1 - W
    print "C := " + str(C) + " M := " + str(M) + " Y := " + str(Y) + " K := " + str(K)
