#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:54:42 2022

@author: gavinkoma
"""

import sys

np = input("Enter the the highest value to find primes for:  ")


#np = int(sys.argv[1])

def isprime(n):  
    if n == 1:
        print("1 is special")
        return False
    
    for x in range(2,n):
        if n % x == 0:
            #print("{} equals {} x {}".format(n,x,n//x))
            return False
        
    else:
        myfile.write("{}\n".format(n))
        print(n, "is a prime number")
       
        return True
    #myfile.close()

myfile = open('primes.txt','a')

for n in range(1,int(np)):
    isprime(n)
    
    
myfile.close()
if myfile.closed:
  print('file is closed')


##how do we add a runtime parameter N for finding primes
##
