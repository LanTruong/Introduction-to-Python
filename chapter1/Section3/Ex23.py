import random

# Accept integer command-line arguments stake, goal, and trialCount.
# Run trialCount experiments that start with stake dollars and
# terminate on 0 dollars or goal.  Write to standard output the
# percentage of wins and the average number of bets per experiment.

stake = int(raw_input("Enter the initial stake: "))
goal = int(raw_input("Enter goal: "))
trials = int(raw_input("Enter number of trials: "))
p = float(raw_input("Enter a probability (number in range(0,1)): "))
bet = int(raw_input("Enter number of bets: "))
# Run trialCount experiments that start with stake and terminate on
# 0 or goal.
bets = 0
wins = 0
for t in range(trials):
    # Run one experiment.
    cash = stake
    while cash > 0 and cash < goal:
        # Simulate one bet.
        bets += 1
        if random.random() > (1-p):
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

print str(100 * wins//trials) + '% wins'
print 'Avg # bets: ' + str(bets//trials)
