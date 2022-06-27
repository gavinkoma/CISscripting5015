#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:56:06 2022

@author: gavinkoma
"""
import random
import time

#create our 5000 numbers at the start
list5000 = []
for xeta in range(0,5000):
    xeta = random.randint(0,5000)
    list5000.append(xeta)

#split list into two random sects for later use
listone = list5000[:2500]
listtwo = list5000[2500:]



#%% sort 5000 values 

def main():
    bubble_sort(list5000)

#this is the python code for bubble sort

#https://www.javatpoint.com/bubble-sort-in-python

# Creating a bubble sort function  
def bubble_sort(list5000):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list5000)-1):  
        for j in range(len(list5000)-1):  
            if(list5000[j]>list5000[j+1]):  
                temp = list5000[j]  
                list5000[j] = list5000[j+1]  
                list5000[j+1] = temp  

    return list5000  

startmain = time.time()

main()
#calling the list itself
print("The unsorted list is: ", list5000)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list5000))
  
endmain = time.time()

print(endmain-startmain)

#%%

def main():
    bubble_sortlistone(listone)
    bubble_sortlisttwo(listtwo)    

# Creating a bubble sort function  
def bubble_sortlistone(listone):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(listone)-1):  
        for j in range(len(listone)-1):  
            if(listone[j]>listone[j+1]):  
                temp = listone[j]  
                listone[j] = listone[j+1]  
                listone[j+1] = temp  
    return listone


# Creating a bubble sort function  
def bubble_sortlisttwo(listtwo):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(listtwo)-1):  
        for j in range(len(listtwo)-1):  
            if(listtwo[j]>listtwo[j+1]):  
                temp = listtwo[j]  
                listtwo[j] = listtwo[j+1]  
                listtwo[j+1] = temp  
    return listtwo


startmerge = time.time()

main()

#merge and sort the lists now; lets do a smaller list first just to make sure it works
merged_sorted = []

lengthone = len(listone)
lengthtwo = len(listtwo)

merged_sorted = []
xeta,zed = 0,0

while xeta < lengthone and zed < lengthtwo:
    if listone[xeta] < listtwo[zed]:
        merged_sorted.append(listone[xeta])
        xeta += 1
        
    else:
        merged_sorted.append(listtwo[zed])
        zed += 1
merged_sorted = merged_sorted + listone[xeta:] + listtwo[zed:]        

endmerge = time.time()
print(endmerge-startmerge)
    


#%% compare lists

if merged_sorted == list5000:
    print("lists are identical")
else:
    print("lists are not the same")

    
  



