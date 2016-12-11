#dragon curve
#Description: A dragon curve of orfer n is a curve of order n-1
#followed by an L followed by a curve of order n-1 traversed in reverse order

def InverseDragonCurve(n):
    if (n==0):
        return "F"
    else:
        return DragonCurve(n-1) + "R" + InverseDragonCurve(n-1)
def DragonCurve(n):
    if (n == 0):
        return "F"
    else:
        return DragonCurve(n-1) + "L" + InverseDragonCurve(n-1)

def DragonCurve_(n):
    f = "F"
    r = "F"
    for i in range(0,n):
        f0 = f + "L" + r
        r0 = f + "R" + r
        f = f0
        r = r0
    return f
n = int(raw_input("Enter the order of the curve: "))
option = int(raw_input("Which method do you use: (1 : recursion, 2 : for loop ): "))
if (option == 1):
    print DragonCurve(n)
elif (option == 2):
    print DragonCurve_(n)
else:
    print "Unknown option."
