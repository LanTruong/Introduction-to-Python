#find gcd(x,y)
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
x = int(raw_input("Enter a number: "))
y = int(raw_input("Enter a number: "))
print gcd(x,y)
