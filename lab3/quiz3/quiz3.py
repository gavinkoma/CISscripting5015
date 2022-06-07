#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:07:00 2022

@author: gavinkoma
"""

#%% calculate the remainder

n = 99
d = 5
q = n//d
r = n%d
print("Quotient: " + str(q))
print("Remainder: " + str(r))

#%% question 4
word = "Hello World"


#%% question 5
A=['car','truck','1234','7777']

#%%question 6

words=['car','truck','window','defenestrate']
print(words)

for w in words[:]:

    if (len(w))>6:

        words.insert(0,w)
        print(words)