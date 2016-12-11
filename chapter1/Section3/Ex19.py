# Accept integer i and k as two command-line argument. 
# Convert i in base k

# Limitation: Does not handle negative integers.

i = int(raw_input("Enter i: "))
k = int(raw_input("Enter k: "))

# Compute v as the largest power of k <= n.


def BaseNumber(k):
    if (0<=k and k<10):
        return str(k)
    elif (k==10):
        return "A"
    elif (k==11):
        return "B"
    elif (k==12):
        return "C"
    elif (k==13):
        return "D"
    elif (k==14):
        return "E"
    elif (k==15):
        return "F"
     

s = ""
# Cast out powers of 2 in decreasing order.
while i > 0:
    s = BaseNumber(i%k) + s
    i = i/k
print s


