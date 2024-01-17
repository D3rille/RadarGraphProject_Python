#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
from playerinfos import entry_alpha, entry_numeric, position
from statentry import graph_stat, stat_entry, set_val
from radargraph import radar_factory

print("Welcome to the Athlete Performance Grapher!")

while True:
    print("Choose: Type \"single\" for single stat display mode and Type \"multi\" for stat comparison mode.")
    mode= input("Type mode: ").lower().strip(" ")
    if mode == "multi" or mode == "single":
        break
    else:
        print("Invalid entry.")
        continue
        
if mode=="single":
    num=1
    
else:
    while True:
        num=int(input("Enter number of players to be compared(max is 3): "))
        if num==3 or num==2:
            break            
        elif num>3:
            print("Exceeded maximum entry, Input a lower number")
        else:
            print("Enter a number higher than zero.")


data = [["Scoring", "Assisting", "Rebounding", "Blocking", "Stealing"],
        ('Player Stats', [])]

playerInfos=[]
playerStats=[]

for x in range(num):
    if x>=1:
        print()
        print("Next Player: ")
    infos= {"name":'', "age":'',"position":'', "height":'', "weight":'', "matches":''}
    playerInfos.append(infos)
    #to enter player's personal information
    for info in infos:
        if info=="name":
            prompt="Enter the name of the player: "
            entry_alpha(infos, info, prompt)
        elif info=="age":
            prompt="Enter the age of the player: "
            entry_numeric(infos, info, prompt)
        elif info=="position":
            prompt="Enter the main position played by the player: "
            while True:
                entry_alpha(infos, info, prompt)
                t=position(infos)
                if t==False:
                    break
                else:
                    continue
        elif info=="height":
            prompt="Enter the height of the player(cm): "
            entry_numeric(infos, info, prompt)
        elif info=="weight":
            prompt="Enter the weight of the player(kg): "
            entry_numeric(infos, info, prompt)
        elif info=="matches":
            prompt="Enter the number of matches played: "
            entry_numeric(infos, info, prompt)



    aveStats={"Scoring":0, "Assisting":0, "Rebounding":0,"Blocking":0, "Stealing":0}


    #Values for max_value in def graph_stat
    maxValues=[30.12, 11.19, 22.89, 3.50, 2.71]

    #to enter player's statistical data
    for stat in aveStats:
        while stat=="Scoring":
            print("Select input option: entry Total or entry multiple data")
            selectedOpt=input("Type 1 for entry total, 2 for multiple entry: ")
            if selectedOpt=="1" or selectedOpt=="2":
                break
            else:
                print("Invalid entry, Try again")

        while True:
            print()
            print(stat, "Statistic:")
            break        
        if stat=="Scoring":
            prompt="Enter Score"
            stat_entry(selectedOpt, aveStats, stat, int(infos["matches"]), prompt)
            scoring=round(graph_stat(aveStats[stat],maxValues[0] ),2)
            scoring=set_val(scoring)
        elif stat=="Assisting":
            prompt="Enter Assists"
            stat_entry(selectedOpt, aveStats, stat, int(infos["matches"]), prompt)
            assisting=round(graph_stat(aveStats[stat], maxValues[1]),2)
            assisting=set_val(assisting)
        elif stat=="Rebounding":
            prompt="Enter Rebounds"
            stat_entry(selectedOpt, aveStats, stat, int(infos["matches"]), prompt)
            rebounding=round(graph_stat(aveStats[stat], maxValues[2]), 2)
            rebounding=set_val(rebounding)
        elif stat=="Blocking":
            prompt="Enter Blocks"
            stat_entry(selectedOpt, aveStats, stat, int(infos["matches"]), prompt)
            blocking=round(graph_stat(aveStats[stat], maxValues[3]), 2)
            blocking=set_val(blocking)
        elif stat=="Stealing":
            prompt="Enter Steals"
            stat_entry(selectedOpt, aveStats, stat, int(infos["matches"]), prompt)
            stealing=set_val(round(graph_stat(aveStats[stat], maxValues[4]), 2))
            stealing= set_val(stealing)
    playerStats.append(aveStats)        
    statistics=[scoring, assisting, rebounding, blocking, stealing]
    data[1][1].append(statistics)

#for making the radar graph
N = len(data[0])
theta = radar_factory(N, frame='polygon')

spoke_labels = data.pop(0)
title, stat_data = data[0]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='radar'))
fig.subplots_adjust(top=0.85, bottom=0.05)
ax.set_ylim(0,1.0)

ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
ax.set_title(title,  position=(0.5, 1.1), ha='center')

colors = ['b', 'r', 'g', 'm', 'y']


for d, color in zip(stat_data,colors):
    line = ax.plot(theta, d, color=color)
    ax.fill(theta, d,  alpha=0.25)
    ax.scatter(theta, d, color=color)
    
     
def legend_name(playerInfos=playerInfos):
    #for getting first name for legends in multi mode
    names=[] 
    for i in range(len(playerInfos)):
        firstName= playerInfos[i]["name"].split(" ")
        names.append(firstName[0])
    return names
        
names=legend_name()

if  mode=="multi":   
    if len(names)==2:
        labels = (names[0], names[1])
    elif len(names)==3:
        labels=(names[0], names[1], names[2])
    legend = ax.legend(labels, loc=(0.8, 0.95),
                        labelspacing=0.1, fontsize='medium')
    

def get_infoStats(playerStats, playerInfos):
        line1= "Name: "+ playerInfos.get("name")+"     "+"age: "+ playerInfos.get("age")
        line2= "Position: "+ playerInfos.get("position")
        line3= "Height: "+ playerInfos.get("height")+"cm"+"     "+"Weight: "+playerInfos.get("weight")+"kg"
        line4= "Matches: "+ playerInfos.get("matches")
        lines1=[line1, line2, line3, line4]

        line5= "Scores per game: "+ str(round(playerStats.get("Scoring"),2))
        line6= "Assists per game: "+ str(round(playerStats.get("Assisting"),2))
        line7= "Rebounds per game: "+str(round(playerStats.get("Rebounding"),2))
        line8= "Blocking per game: "+ str(round(playerStats.get("Blocking"),2))
        line9= "Steals per game: "+ str(round(playerStats.get("Stealing"),2))
        lines2=[line5, line6, line7, line8, line9]
        
        return lines1, lines2

def place_infoStats(lines1, lines2, points, loopVar,  xaxis1=1.0, xaxis2=1.5, num=num):
    if num>1:
        x=xaxis2 
    else:
        x=xaxis1
    if e>0:
        f=points[loopVar]
    else:
        f=0.90
        
    for c in range(4):
        fig.text(xaxis1, f, lines1[c],
                 horizontalalignment='left', color='black', weight='medium',
                 size='large')
        f-=0.04
    if num==1:
        g=0.60
    elif e>=0:
        g=points[loopVar]
        
    for b in range(5):
        fig.text(x, g, lines2[b],
                horizontalalignment='left', color='black', weight='medium',
                size='large')
        g-=0.04
        
        
for e in range(num):
    startPoints=[0.90, 0.60, 0.30]
    lines1, lines2 = get_infoStats(playerStats[e], playerInfos[e])
    place_infoStats(lines1, lines2, startPoints, e)
    
    
ax.set_varlabels(spoke_labels)

plt.show()

