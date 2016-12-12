def Product_Of_Matrix(a,b):
    if len(a[0]) == len(b):
        c = [[0.0 for i in range(0,len(a))] for j in range(0,len(b[0]))]
        for i in range(len(c)):
            for j in range(len(c[0])):
                for k in range(len(a[0])):
                   c[i][j] += (a[i][k] * b[k][j])
        return c
    else:
        return "These matrix are not matched."
#Test
print "Test 1: "    
a = [[1,2,4],[2,1,1]]
b = [[1,0],[0,1],[1,1],[0,0]]
print Product_Of_Matrix(a,b)

print "Test 2: " 
a = [[1,2,4],[2,1,1]]
b = [[1,0],[0,1],[1,1]]
print Product_Of_Matrix(a,b)
