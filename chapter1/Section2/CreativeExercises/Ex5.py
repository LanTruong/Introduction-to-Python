#order check whether three inputs in ascending or descending order
x = float(raw_input("Enter x: "))
y = float(raw_input("Enter y: "))
z = float(raw_input("Enter z: "))

if (((x < y) and (y < z)) or ((x > y) and (y > z))):
    print "True"
else:
    print "False"
