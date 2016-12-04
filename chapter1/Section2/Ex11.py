##input two integers and check whether if either divides evenly the other.
input1 = int(raw_input("Enter first input: "))
input2 = int(raw_input("Enter second input: "))

quo1 = input1/input2
quo2 = input2/input1

if ((quo1 * input2 == input1) or (quo2 * input1 == input2)):
    print "True"
else:
    print "False"
