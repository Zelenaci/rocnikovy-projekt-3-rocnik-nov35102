# -*- coding: utf-8 -*-
"""
Created on Wed May 21 7:16:47 2018

@author: tom11
"""



import random
ted = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
inducerlist = [0,1,2,3]
ted[random.choice(inducerlist)][random.choice(inducerlist)]=2
def users_choice(ted,zdroj_input):
    
if zdroj_input == "u":
        
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
                        
 
                        
 
          
 
    

