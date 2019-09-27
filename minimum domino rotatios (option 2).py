from collections import defaultdict
"""
:type A: List[int]
:type B: List[int]
:rtype: int
"""
A=[2,1,2,4,2,2]
B=[5,2,6,2,3,2]
n = len(A)
dicA = defaultdict(int)
dicB = defaultdict(int)
dup = defaultdict(int)

#counting each number and registring the duplicates
for i in range(n):
    dicA[A[i]] += 1
    dicB[B[i]] += 1
    if A[i] == B[i]:
        dup[A[i]] += 1

# initializing the result
res = float('inf')

#looping through it
for key,val in dicA.items():
    #if it is already flipped
    if val == n:
        print(0)
    #the the count for that number in both dictionaries subtracted by the duplicates is more than or equal to n
    if val + dicB[key] - dup[key] == n:
        res = min(res,n - val,n - dicB[key])

#if the value hasn't change it means it didn't go into the if statement meaning there is not at least one viable solution
print(res if res != float('inf') else -1)