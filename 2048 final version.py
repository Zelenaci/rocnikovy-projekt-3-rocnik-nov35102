
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 7:16:47 2018

@author: tom11
"""



import random
ted = [[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]

inducerlist = [0,1,2,3]
ted[random.choice(inducerlist)][random.choice(inducerlist)]=2
def users_choice(ted,user_input):
    if user_input == "w": 
        i=0
        for j in range(0,4):
            if ted[i][j]!=0 or ted[i+1][j]!=0 or ted[i+2][j]!=0 or ted[i+3][j]!=0:               
                if ted[i][j]==0:
                    while ted[i][j]==0:
                        ted[i][j]=ted[i+1][j]
                        ted[i+1][j]=ted[i+2][j]
                        ted[i+2][j] = ted[i+3][j]
                        ted[i+3][j]=0
                if ted[i+1][j]==0 and (ted[i+2][j]!=0 or ted[i+3][j]!=0):
                    while ted[i+1][j]==0:
                        ted[i+1][j]=ted[i+2][j]
                        ted[i+2][j]=ted[i+3][j]
                        ted[i+3][j]=0
                if ted[i+2][j]==0 and (ted[i+3][j]!=0):
                    while ted[i+2][j]==0:
                        ted[i+2][j]=ted[i+3][j]
                        ted[i+3][j]=0
        
        i=0
        for j in range(0,4):
            if ted[i][j]==ted[i+1][j]:
                ted[i][j]=ted[i][j]+ted[i+1][j]
                ted[i+1][j]=ted[i+2][j]
                ted[i+2][j]=ted[i+3][j]
                ted[i+3][j]=0
            if ted[i+1][j]==ted[i+2][j]:
                ted[i+1][j]=ted[i+1][j]+ted[i+2][j]
                ted[i+2][j]=ted[i+3][j]
                ted[i+3][j]=0
            if ted[i+2][j]==ted[i+3][j]:
                ted[i+2][j]=ted[i+2][j]+ted[i+3][j]
                ted[i+3][j]=0
    elif user_input == "s":
        i=0
        for j in range(0,4):
            if ted[i][j]!=0 or ted[i+1][j]!=0 or ted[i+2][j]!=0 or ted[i+3][j]!=0:
                if ted[i+3][j]==0:
                    while ted[i+3][j]==0:
                        ted[i+3][j]=ted[i+2][j]
                        ted[i+2][j]=ted[i+1][j]
                        ted[i+1][j]=ted[i][j]
                        ted[i][j]=0
                if ted[i+2][j]==0 and (ted[i+1][j]!=0 or ted[i][j]!=0):
                    while ted[i+2][j]==0:
                        ted[i+2][j]=ted[i+1][j]
                        ted[i+1][j]=ted[i][j]
                        ted[i][j]=0
                if ted[i+1][j]==0 and ted[i][j]!=0:
                    while ted[i+1][j]==0:
                        ted[i+1][j]=ted[i][j]
                        ted[i][j]=0
        i=0
        for j in range(0,4):
            if ted[i+3][j]==ted[i+2][j]:
                ted[i+3][j]=ted[i+3][j] + ted[i+2][j]
                ted[i+2][j]=ted[i+1][j]
                ted[i+1][j]=ted[i][j]
                ted[i][j]=0
            if ted[i+2][j]==ted[i+1][j]:
                ted[i+2][j]=ted[i+2][j]+ted[i+1][j]
                ted[i+1][j]=ted[i][j]
                ted[i][j]=0
            if ted[i+1][j]==ted[i][j]:
                ted[i+1][j]=ted[i+1][j]+ted[i][j]
                ted[i][j]=0
            
    elif user_input == "a":
        j=0
        for i in range(0,4):
            if ted[i][j]!=0 or ted[i][j+1]!=0 or ted[i][j+2]!=0 or ted[i][j+3]!=0:
                if ted[i][j]==0:
                    while ted[i][j]==0:
                        ted[i][j]=ted[i][j+1]
                        ted[i][j+1]=ted[i][j+2]
                        ted[i][j+2] = ted[i][j+3]
                        ted[i][j+3]=0
                if ted[i][j+1]==0 and (ted[i][j+2]!=0 or ted[i][j+3]!=0):
                    while ted[i][j+1]==0:
                        ted[i][j+1]=ted[i][j+2]
                        ted[i][j+2]=ted[i][j+3]
                        ted[i][j+3]=0
                if ted[i][j+2]==0 and (ted[i][j+3]!=0):
                    while ted[i][j+2]==0:
                        ted[i][j+2]=ted[i][j+3]
                        ted[i][j+3]=0
        j=0
        for i in range(0,4):
            if ted[i][j]==ted[i][j+1]:
                ted[i][j]=ted[i][j]+ted[i][j+1]
                ted[i][j+1]=ted[i][j+2]
                ted[i][j+2]=ted[i][j+3]
                ted[i][j+3]=0
            if ted[i][j+1]==ted[i][j+2]:
                ted[i][j+1]=ted[i][j+1]+ted[i][j+2]
                ted[i][j+2]=ted[i][j+3]
                ted[i][j+3]=0
            if ted[i][j+2]==ted[i][j+3]:
                ted[i][j+2]=ted[i][j+2]+ted[i][j+3]
                ted[i][j+3]=0
    elif user_input == "d":
        j=0
        for i in range(0,4):
            if ted[i][j]!=0 or ted[i][j+1]!=0 or ted[i][j+2]!=0 or ted[i][j+3]!=0:
                if ted[i][j+3]==0:
                    while ted[i][j+3]==0:
                        ted[i][j+3]=ted[i][j+2]
                        ted[i][j+2]=ted[i][j+1]
                        ted[i][j+1]=ted[i][j]
                        ted[i][j]=0
                if ted[i][j+2]==0 and (ted[i][j+1]!=0 or ted[i][j]!=0):
                    while ted[i][j+2]==0:
                        ted[i][j+2]=ted[i][j+1]
                        ted[i][j+1]=ted[i][j]
                        ted[i][j]=0
                if ted[i][j+1]==0 and ted[i][j]!=0:
                    while ted[i][j+1]==0:
                        ted[i][j+1]=ted[i][j]
                        ted[i][j]=0
        j=0
        for i in range(0,4):
            if ted[i][j+3]==ted[i][j+2]:
                ted[i][j+3]=ted[i][j+3] + ted[i][j+2]
                ted[i][j+2]=ted[i][j+1]
                ted[i][j+1]=ted[i][j]
                ted[i][j]=0
            if ted[i][j+2]==ted[i][j+1]:
                ted[i][j+2]=ted[i][j+2]+ted[i][j+1]
                ted[i][j+1]=ted[i][j]
                ted[i][j]=0
            if ted[i][j+1]==ted[i][j]:
                ted[i][j+1]=ted[i][j+1]+ted[i][j]
                ted[i][j]=0
                
 
while True:
    print(ted[0][0],"\t",ted[0][1],"\t",ted[0][2],"\t",ted[0][3],"\n")
    print(ted[1][0],"\t",ted[1][1],"\t",ted[1][2],"\t",ted[1][3],"\n")
    print(ted[2][0],"\t",ted[2][1],"\t",ted[2][2],"\t",ted[2][3],"\n")
    print(ted[3][0],"\t",ted[3][1],"\t",ted[3][2],"\t",ted[3][3],"\n")
    user_input = input("w for nahoru, s for dolu, a for doleva and d for doprava")
    users_choice(ted,user_input)
    listfori = []
    listforj = []
    count = 0
    for i in range(0,4):
        for j in range(0,4):
            if ted[i][j]==0:
                count+=1
                listfori.append(i)
                listforj.append(j)
    if count > 0:
        if count > 1:
            randomindex = listfori.index(random.choice(listfori))
            ted[listfori[randomindex]][listforj[randomindex]]=2
        else:
            ted[listfori[0]][listforj[0]]=2
    else:
        break
print("Konec")
