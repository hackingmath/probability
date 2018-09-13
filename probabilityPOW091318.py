'''Center of Math POW
https://twitter.com/centerofmath/status/1040229871618809856
September 13, 2018
Events:
probability of A = 0.2
probability of B = 0.3

find P(C), probability that at least one of A or B occurs
find P(D), probability that exactly one of A or B occurs
find P(A|D) and determine whether A and D are independent
'''

from random import random

N_TRIALS = 1000000

trialList = []
for i in range(N_TRIALS):
    trial = []
    randA = random()
    randB = random()
    if randA <= 0.2:
        trial.append(1)
    else:
        trial.append(0)
    if randB <= 0.3:
        trial.append(1)
    else:
        trial.append(0)

    trialList.append(trial)

#print(trialList)
As = 0 #number of times A occurs
Bs = 0 #number of times B occurs
Cs = 0 #at least 1 of A or B
Ds = 0 #exactly 1 of A or B
A_given_D = 0
B_given_D = 0

for trial in trialList:
    if trial[0]:
        As += 1
    if trial[1]:
        Bs += 1
    if 1 in trial:
        Cs += 1
    if sum(trial) == 1:
        Ds += 1
        if trial[0]:
            A_given_D += 1
        if trial[1]:
            B_given_D += 1

P_D = Ds/N_TRIALS

print("P(A):",As/N_TRIALS)
print("P(B):",Bs/N_TRIALS)
print("P(C):",Cs/N_TRIALS)
print("P(Exactly 1):",P_D)
print("P(A|D):",(A_given_D/(N_TRIALS*P_D)))
print("P(B|D):",B_given_D/(N_TRIALS*P_D))


