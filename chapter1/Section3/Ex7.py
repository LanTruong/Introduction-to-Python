#print out numbers in range [1000,2000) with five integers per lines
s =""
for i in range(1000,2000):
    s += str(i)+ " "
    if (i%5) == 4:
        print s
        s = ""
