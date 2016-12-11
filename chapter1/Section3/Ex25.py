n = int(raw_input("Enter a number: "))
factor = 2
pre = 1
s = ""
while factor*factor <= n:
    while n % factor == 0:
        # Cast out and write factor.
        n /= factor
        if factor > pre:
            s += str(factor) + " "
            pre = factor
    factor += 1
    # Any factors of n are greater than or equal to factor.

if n > 1:
    s += str(n)
print s
