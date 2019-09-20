
from collections import Counter
a=[1,2,1,1,1,2,2,2]
b=[2,1,2,2,2,2,2,2]
common=Counter(a).most_common(1)[0][0] #counts all occurrences for each number and returns the one that has more occurrences
rotations=0
for i,value in enumerate(a):
    if value==common:
        pass
    else:
        if b[i]==common:
            rotations+=1
            a[i]=b[i] #replace the value in a with b
if Counter(a).most_common(1)[0][1] == len(a):
    print(rotations)
else: #do the same with b list
    #initialize variables
    rotations=0
    a=[1,2,1,1,1,2,2,2]
    b=[2,1,2,2,2,2,2,2]
    common=Counter(b).most_common(1)[0][0] #counts all occurrences for each number and returns the one that has more occurrences
    for i,value in enumerate(b):
        if value==common:
            pass
        else:
            if a[i]==common:
                rotations+=1
                b[i]=a[i] #replace the value in a with b
    if Counter(b).most_common(1)[0][1] == len(b):
        print(rotations)
    else:
        print(-1)
