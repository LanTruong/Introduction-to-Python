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

n = int(raw_input("Enter a number: "))
a = [[True for i in range(0,n)]for j in range(0,n)]
for i in range(1,n+1):
    for j in range(i,n+1):
        if (gcd(i,j)>1):
            a[i-1][j-1] = False
            a[j-1][i-1] = False
print a
for i in range(0,n):
    s = ""
    for j in range(0,n):
        if (a[i][j] == False):
            s += " "
        else:
            s += "*"
    print s
