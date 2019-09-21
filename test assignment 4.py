import numpy as np
array=np.arange(0,35)
while True:
    indexes=np.arange(0,len(array))
    choices=np.random.choice(indexes, 4)
    sortChoices=sorted(choices)
    diffChoices=np.diff(sortChoices)
    if 0 in diffChoices:
        #index repeated, pick another 4
        continue
    elif 1 in diffChoices:
        #index consecutive, pick another 4
        continue
    else:
        print(sortChoices)