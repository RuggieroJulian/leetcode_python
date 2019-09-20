# -*- coding: utf-8 -*-


def steps(f,c):
    '''
    Created on Thu Sep 19 23:57:09 2019
    This function takes a list of integers (flowers) and an integer (capacity)
    Each integer represents the amount of water that this flower needs, if not
    enough water it goes to refill(0 index) and then is able to apply the water.
        - water the plants in the order in which they appear, from left to right;
        - water each plant if you have sufficient water for it, otherwise refill your watering can;
        - water each plant in one go, i.e. without taking a break to refill the watering can in the middle of watering a single plant. This means that you may sometimes have to refill your watering can before or after watering a plant, even though it's not completely empty.
    You start at the water container, which is positioned one step before the first plant. How many steps will you take, in order to water all the plants in the row? You must take one step to move to the next or the previous plant (all plants are positioned one step apart from each other).
    @author: julian ruggiero
    '''
    flowers=f
    capacity=c
    #add the capacity at the end, and then invert the list to have it at the beginning
    flowers.insert(0,capacity)

    steps=0
    reminder=6
    finish=False
    filled=[]
    filled.append(0) #index 0 for the capacity added
    i=1
    while finish != True:
        if len(filled)==len(flowers):
            finish=True
            continue
        else:
            #index has not been filled yet
            if i not in filled:
                if flowers[i]<=reminder:
                    filled.append(i)
                    reminder-=flowers[i]
                    steps+=1
                    i+=1
                else:
                    #go back to fill and return to the same position
                    steps+=(i*2)-2
                    reminder+=capacity
                    
                    continue
    return steps
steps([2,4,5,1,2],6)