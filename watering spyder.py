# -*- coding: utf-8 -*-

c=6
f=[2,4,5,1,2]
steps=0
reminder=c
for i,value in enumerate(f):
    if reminder>=value:
        steps+=1
        reminder-=value
    else:
        steps+=(i*2)+1
        reminder+=c
        reminder-=value
print(steps)