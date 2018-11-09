# -*- coding: utf-8 -*-
"""
This python code calculates the number of 1-1, 1-many mappings and also the number of no-mapping terms both in ICD9 to 10 and ICD10 to 9.
It needs the paths to '2018_I9gem.txt' and '2018_I10gem.txt' files as input and prints the number of mentioned mappings as the output.

@author: Parisa Sarikhani
"""

import sys

def  ICD_flags(path1,path2):
    #read ICD9-10 file:
    fo=open(path1 ,'r')
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
    fo=open(path2,'r')
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
    
    ICD_flags(sys.argv[1],sys.argv[2])
        
    
