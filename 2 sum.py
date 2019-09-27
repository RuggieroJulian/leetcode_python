target=6
vector=[3,2,4]
leng=len(vector)
result=[]
complement={}
for i,value in enumerate(vector):
    diff=target-value
    if value in complement.keys():
        result.append(complement[value])
        result.append(i)
    if value in complement.keys():
        continue
        else:
            #store the complement, continue looking
            complement[diff]=i