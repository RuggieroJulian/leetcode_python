from collections import defaultdict
s="egg"
t="add"
d={}
for cs,ct in zip(s,t):
    if cs not in d:
        if ct in d.values():
            print(False)
        d[cs]=ct
    elif d[cs]!=ct:
            print(False)
print(True)