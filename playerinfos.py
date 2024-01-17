#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#functions for player's personal information entry
def entry_alpha(dictionary, loopVar, prompt):
#for entry and validation of alphabet input
    #for entry alphabet entry
    while True:
        dictionary[loopVar]=input(prompt).strip(" ")
        dictionary[loopVar]= dictionary[loopVar].title()
        #for validating alphabet entry
        for x in dictionary[loopVar]:
            if x.isalpha()==True or x==" ":
                t=False
            elif x==".":
                t=False
            else:
                t=True
                break
        if t==False:
                break
        else:
            print("Invalid entry, Try again")

positions=[["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"],
          ["PG", "SG","SF", "PF", "C"]]

def position(dictionary, pos=positions):# to validate or determine position of the player
    #If entry is more than two characters
    if len(dictionary["position"])>2:
        if positions[0].count(dictionary["position"])==1:
            return False
    #If entry has a one or two characters or an acronym
    elif len(dictionary["position"])<=2 and len(dictionary["position"])>0:
        dictionary["position"]=dictionary["position"].upper()
        if positions[1].count(dictionary["position"])==1:
            return False
        else:
            print("No position exist... try again")
    else:
        print("No position exist... try again")


def entry_numeric(dictionary, loopVar, prompt):
#for entry and validation of numeric input
    #for entry of numeric input
    while True:
        dictionary[loopVar]=input(prompt).strip(" ")
        #for validating numeric entry
        for x in dictionary[loopVar]:
            t=True
            if dictionary[loopVar][-1::]==".":
                break
            if x.isnumeric()==True:
                t=False
            elif x==".":
                continue
            else:
                t=True
                break
        if t==False:
            break
        else:
            print("Invalid entry, Try again")
        

