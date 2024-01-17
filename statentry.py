#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#functions for statistics entry
def average(_list_, numMatches):
    #to determine the average of player based on number of matches
    if 0<len(_list_)<10:
        return sum(_list_)/numMatches
    elif 0<len(_list_)>=10:
        return sum(_list_)/numMatches
    
def graph_stat(part, whole): 
    # to compute the value needed for the graph
    #whole is the maximum value or the highest value for each stat derived from all-time records of the NBA
    return round(part/whole, 2)

def stat_entry(selOpt, aveStats, stat, numMatches, prompt):
    # to determine the the mode of entry
    if selOpt=="1":
        single_statEntry(aveStats, stat, numMatches, prompt)
    elif selOpt=="2":
        multiple_statEntry(aveStats, stat,numMatches, prompt)
    else:
        print("Invalid entry, Try again")
        
        
def multiple_statEntry(dictionary, loopVar, numMatches, prompt):
    # for multi-stat entry, entering stats for each matches
    scores=[]
    for y in range(numMatches):
        while True:
            score=input(prompt+"["+str(y+1)+"]: ").strip(" ")
            for x in score:
                t=True
                if score[-1::]==".":
                    break
                if x.isnumeric()==True:
                    t=False
                elif x==".":
                    continue
                else:
                    t=True
                    break
            if t==False:
                scores.append(int(score))
                break
            else:
                print("Invalid entry, Try again")
    dictionary[loopVar]=average(scores, numMatches)
            
def single_statEntry(dictionary, loopVar, numMatches, prompt):
    # for single-entry, entering total stats based from the number of matches
    scores=[]
    t=True
    while t:
        score= input(prompt+"(Total): ").strip(" ")
        for x in score:
            t=True
            if score[-1::]==".":
                break
            if x.isnumeric()==True:
                t=False
            elif x==".":
                continue
            else:
                t=True
                break
        if t==False:
            scores.append(int(score))
        else:
            print("Invalid entry, Try again")
    dictionary[loopVar]= average(scores, numMatches)

def set_val(stat, limit=1.0):
    #to set value to max if value computed is greater than the max or the limit
    if stat >= limit:
        return limit
    else:
        return stat        
        

