# new solution by myself
from collections import Counter, defaultdict
secret='011'
guess='110'
numbersA=0
numbersB=0
secretCount=Counter(secret)
guessCount=Counter(guess)
#using defaultdict to be able to increment without initializing
dictA=defaultdict(int)

#finding the Bulls (match position and digit)
for i,value in enumerate(secret):
    if secret[i] == guess[i]:
        numbersA+=1
        dictA[value]=+1
        
#finding cows, matches digit only
for i,value in secretCount.items():
    if value in dictA.keys():
        #matching position, looking if same number more times
        reminder=secretCount[value]-dictA[value]
        if guessCount[value] >= reminder:
            numbersB+=reminder
        else:
            numbersB+=guessCount[value]
    elif value in guessCount.keys():
        if guessCount[value] >= secretCount[value]:
            numbersB+=guessCount[value]
        else:
            numbersB+=secretCount[value]
print(numbersA, numbersB)