import numpy as np
import collections
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr,swaps):
    if swaps==0:
        arra=[items-1 for items in arr]
        print(arr,swaps)
    else:
        print(arr,swaps)
        
        arra=arr
    #print(arra)
    for i in range(len(arra)-1):
        tup = collections.Counter(np.diff(arra)).most_common(1)[0]
        print(tup)
        if tup[0] == 1 and tup[1] == len(arra):
            return swaps
        if i==arra[i]:
            continue
        elif (i==len(arra)-1):
            break
        elif arra[i]>arra[i+1]:
            swaps+=1
            arra[i],arra[i+1]=arra[i+1],arra[i]
            #reset i if necesary, because even doing the swap it is still not in the position that corresponds
            if arra[i]<i:
                print("recursion ",arra,swaps)
                minimumSwaps(arra,swaps)
            #print(arra,swaps)
    return swaps



if __name__ == '__main__':
    res = minimumSwaps([1,3,5,2,4,6,7],0)