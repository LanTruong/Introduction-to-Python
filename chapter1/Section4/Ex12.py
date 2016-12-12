#transpose of an array
def transpose(a):
    b = [[0.0 for i in range(0,len(a))] for j in range(0,len(a[0]))]
    for i in range(0,len(b)):
        for j in range(0,len(b[0])):
            b[i][j] = a[j][i]            
    return b

#Test
a = [[i for i in range(0,2)] for j in range(0,3)]
print a
print transpose(a)
