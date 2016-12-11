def gcd(x,y):    
    if x <= y:
        u = x
        x = y
        y = u
    while (y > 1):
        u = x%y
        x = y
        y = u
        
    if (y == 0):
        return x
    else:
        return y
n = int(raw_input("Enter a number :"))
for i in range(1,n+1):
    s = ""
    for j in range(1,n+1):
        if gcd(i,j) == 1:
            s += "*"
        else:
            s += " "
    print s
