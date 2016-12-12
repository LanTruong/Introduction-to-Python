# Accept integers n and trialCount as command-line arguments. Do
# trialCount random self-avoiding walks in an n-by-n lattice. 
# Write to standard output the percentage of dead ends encountered.
import random
n      = int(raw_input("Enter the size of matrix: "))
trials = int(raw_input("Enter the number of trials: "))
deadEnds = 0
dead_area = 0
escape_area = 0
for t in range(trials):
    # Create an n-by-n array, with all elements set to False.
    a = [[False for i in range(0,n)] for j in range(0,n)]
    x = n//2
    y = n//2
    min_x = x
    max_x = x
    min_y = y
    max_y = y
    dead = False
    while (x > 0) and (x < n-1) and (y > 0) and (y < n-1):
        # Check for dead end and make a random move.
        a[x][y] = True
        if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
            deadEnds += 1
            dead = True
            break
        r = random.randrange(1, 5)
        if   (r == 1) and (not a[x+1][y]):
            x += 1
            max_x = x
        elif (r == 2) and (not a[x-1][y]):
            x -= 1
            min_x = x
        elif (r == 3) and (not a[x][y+1]):
            y += 1
            max_y = y
        elif (r == 4) and (not a[x][y-1]):
            y -= 1
            min_y = y
    if dead:
        dead_area += (max_x - min_x)*(max_y - min_y)
    else:
        escape_area += (max_x - min_x)*(max_y - min_y)

print str(100*deadEnds//trials) + '% dead ends'
print "average of dead area: " + str(dead_area/deadEnds)
print "average of escaped area :" + str(escape_area/(trials-deadEnds))

