import random

# Accept integers n and trialCount as command-line arguments. Do
# trialCount random self-avoiding walks in an n-by-n lattice. 
# Write to standard output the percentage of dead ends encountered.

n      = int(raw_input("Enter the size of matrix: "))
trials = int(raw_input("Enter the number of trials: "))
deadEnds = 0
path_sum = 0
escape_path = 0
dead_path = 0
for t in range(trials):

    # Create an n-by-n array, with all elements set to False.
    a = [[False for i in range(0,n)] for j in range(0,n)]
    path = 0
    x = n//2
    y = n//2
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
            path += 1
            x += 1
        elif (r == 2) and (not a[x-1][y]):
            path += 1
            x -= 1
        elif (r == 3) and (not a[x][y+1]):
            y += 1
            path += 1
        elif (r == 4) and (not a[x][y-1]):
            y -= 1
            path += 1
    path_sum += path
    if dead:
        dead_path += path
    else:
        escape_path += path

print str(100*deadEnds//trials) + '% dead ends'
print "average of path :" + str(path_sum/trials)
print "average of dead path :" + str(dead_path/deadEnds)
print "average of escaped path :" + str(escape_path/(trials-deadEnds))

