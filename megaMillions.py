'''Mega Millions Jackpot Night
October 23, 2018
with Jared'''

from random import randint,sample

#first maximum
max1 = 10#70

#second maximum
max2 = 25

#number of choices 1-max1
choices = 3

#number of choices 1-max2
extra = 0

def chooseWinner():
    return sorted(sample(list(range(1,max1+1)),choices)+ \
                  [randint(1,max2) for i in range(extra)])

def chooseTicket():
    ticket = []
    for i in range(choices):
        num = randint(1,max1)
        while num in ticket:
            num = randint(1,max1)
        ticket.append(num)
        sorted(ticket)
    for j in range(extra):
        extra_num = randint(1,max2)
        while extra_num in ticket:
            extra_num = randint(1,max2)
        ticket.append(extra_num)
    return ticket

winner = chooseWinner()
#winner.sort()
print("winner:",winner)

TRIALS = 100000

successes = 0
for i in range(TRIALS):
    trial = chooseTicket()
    #print(trial)
    if trial == winner:
        #print("Success!")
        successes += 1
print("successes:",successes)
print("prob'y:",successes/TRIALS)
