string1 = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
string2 = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
#Creating a dictionary for all the values
dic = {idx:0 for idx,s in enumerate(string2)}
i=0
# Two for loops for both strings.
for s2 in string2:    
    for s1 in string1:
        #checking the number of smallest valued character
        if  s2.count(min(s2)) > s1.count(min(s1)):
            #dictionary sum registry
            dic[i]+=1
    # iterator increment
    i+=1
    #returning only the values in the dictionary and casting them into a list
print([x for i,x in dic.items() if x!=0])
#return list(dic.values()) 