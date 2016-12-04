##take 3 positive integers and check whether they are lengths of triangle
len1 = int(raw_input("Enter first number: "))
len2 = int(raw_input("Enter second number: "))
len3 = int(raw_input("Enter third number: "))

if ((len1 == len2 + len3) or (len2 == len1 + len3) or (len3 == len1 + len2)):
    print "True"
else:
    print "False"
