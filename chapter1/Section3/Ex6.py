#modify tenhello.py
n = int(raw_input("Enter the number of lines: "))

for i in range(1,n+1):
    if ((i % 10) == 1):
        if ((i%100) == 11):
            print str(i) + "th" + " Hello"
        else:
            print str(i) + "st" + " Hello"
    elif ((i%10) == 2):
        if ((i%100) == 12):
            print str(i) + "th" + " Hello"
        else:
            print str(i) + "nd" + " Hello"
    elif ((i%10)==3):
        if ((i%100) == 13):
            print str(i) + "th" + " Hello"
        else:
            print str(i) + "rd" + " Hello"
    else:
        print str(i) + "th" + " Hello"
