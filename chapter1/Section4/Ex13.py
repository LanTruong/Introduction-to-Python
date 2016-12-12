def Product_Of_Bool(a,b):
    c = [[False for i in range(0,len(a))] for j in range(0,len(a))]
    for i in range(len(c)):
        for j in range(len(c)):
            for k in range(len(a)):
               c[i][j] = c[i][j] or (a[i][k] and b[k][j])
    return c

#Test
a = [[True, False],[False, True]]
b = [[False, False], [True, True]]
print a
print b
print Product_Of_Bool(a,b)

