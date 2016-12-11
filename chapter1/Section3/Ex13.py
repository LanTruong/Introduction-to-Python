n = int(raw_input("Enter a number: "))
i = 1
if (n <= 0):
    print "Please type positive number."
else:
    while(i < n):
        print i
        i *=2
