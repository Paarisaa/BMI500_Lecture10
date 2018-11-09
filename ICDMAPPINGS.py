# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:57:57 2018

@author: Parisa Sarikhani
"""

import pandas as pd

def  ICD_flags():
    #read ICD9-10 file:
    fo=open('2018_I9gem.txt','r')
    ICD9=fo.readlines()
    Flags=[]
    for lines in ICD9:
        column=lines.split()
        Flags.append(column[2])#Flags keeps the third column of the text file
        

    #one to ones, one_to_many, and no_map counters
    one_to_one_count=0
    one_to_many_count=0
    no_map_count=0
    for flag in Flags:
        # one-to-one mappings are when we have second flag(no map)=0 and third flag(combination)=0
        if int(flag[1])==0 and int(flag[2])==0:
            one_to_one_count +=1
            # one-to-many mappings are when we have second flag(no map)=0 and third flag(combination)=1
        elif int(flag[1])==0 and int(flag[2])==1:
                one_to_many_count+=1
                # no mappings happen when we have second flag(no map)=1
        elif int(flag[1])==1:
            no_map_count+=1
        
        
    print('Number of one-to-one mappings in ICD9to10: '+str(one_to_one_count))
    print('Number of one-to-many mappings in ICD9to10: '+str(one_to_many_count))
    print('Number of no mappings in ICD9to10: '+str(no_map_count))
        
    ####################################################################
    #read ICD10-9 file:
    fo=open('./2018_I10gem.txt','r')
    ICD10=fo.readlines()
    Flags=[]
    for lines in ICD10:
        column=lines.split()
        Flags.append(column[2])#Flags keeps the third column of the text file
                

    #one to ones, one_to_many, and no_map counters
    one_to_one_count=0
    one_to_many_count=0
    no_map_count=0
    for flag in Flags:
        # one-to-one mappings are when we have second flag(no map)=0 and third flag(combination)=0
        if int(flag[1])==0 and int(flag[2])==0:
            one_to_one_count +=1
            # one-to-many mappings are when we have second flag(no map)=0 and third flag(combination)=1
        elif int(flag[1])==0 and int(flag[2])==1:
            one_to_many_count+=1
            # no mappings happen when we have second flag(no map)=1
        elif int(flag[1])==1:
            no_map_count+=1
        

    print('Number of one-to-one mappings in ICD10to9: '+str(one_to_one_count))
    print('Number of one-to-many mappings in ICD10to9: '+str(one_to_many_count))
    print('Number of no mappings in ICD10to9: '+str(no_map_count))
    
if __name__== "__main__":
    
    ICD_flags()
        
    
