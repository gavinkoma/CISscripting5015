#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 11:49:58 2022

@author: gavinkoma
"""

num = 15



def analysis(num):
    if(num == 15):
        print("N is 15")
        return True
    elif(num<15<num):
        print("N is less than or greater than 15")
    return False

analysis(num)

#%%

list = []

for val in range(5,56):
    list.append(val)
    
print(list)
    
#%% problem 3

x = 15

f = open("problem3.txt","w")
f.write("I wanted to append:\n" + str(x) +"\n to this file")

