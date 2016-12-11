n = int(raw_input("Enter a number: "))
for i in range(1,n+1):
    if (i%2 ==1):
        s = ""
        for i in range(1,n+1):
            s += "* "
        print s
    else:
        s = " "
        for i in range(1,n+1):
            s += "* "
        print s
