#THree-sort
#print three inputs in ascending order
u = []
x1 = float(raw_input("Enter first number: "))
u.append(x1)
x2 = float(raw_input("Enter second number: "))
u.append(x2)
x3 = float(raw_input("Enter third number: "))
u.append(x3)

print "Ascending order: " + str(min(u)) + " " + str(sum(u)-min(u)-max(u)) + " " + str(max(u))
