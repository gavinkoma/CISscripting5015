#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 14:12:06 2022

@author: gavinkoma
"""

#%% question 1 

def rangefunc():
    a = [*range(2,9,2)]
    print(a)


rangefunc()


#%% question 2

print(sum([*range(1,10)]))


#%% question 3

lines = []

stringtoadd = "Ya mum~~"

with open('cormac.txt') as f:
    lines = f.readlines()
    
# =============================================================================
# count = 0
# for line in lines:
#     count += 1
#     print(f'line {count}: {line}')
# =============================================================================
    
new_lines = [line.strip() + stringtoadd for line in lines]
print(new_lines)
    

#%% question 4
#used jupyter lab in class; shared screen for everyone.


#%% question 5 & 6
#the radish question

with open("radishsurvey.txt") as file:
    for line in file:
        line = line.strip() #strips newline
        parts = line.split(" - ") #splits into strings on either side of the hyphen
        name = parts[0] #index
        vote = parts[1] #index
        #print(name+ " voted for " + vote) #print statement
        
#now we can see who voted specifically for white icicle radishes?

count = 0


with open("radishsurvey.txt") as file:
    for line in file:
        line = line.strip()
        name, vote = line.split(" - ")
        if vote == "White Icicle":
            count = count + 1
           # print('White Icicle Count: ' + str(count))
        

#count the votes for a couple different things 
def count_votes(radish):
    print("Counting votes for " + radish + "...")
    count = 0
    with open("radishsurvey.txt") as file:
        for line in file:
            line = line.strip()
            name,vote=line.split(" - ")
            if vote == radish:
                count = count + 1        
    return count

#print(count_votes("Sicily Giant"))

# with open("radishsurvey.txt") as file:
#     for line in file:
#         line = line.strip()
#         name,vote = line.split(" - ")
#         name = name.strip().capitalize().replace("  "," ")
#         print(name + " has already voted!") 
#         continue 
#         voted.append(name)
#         vote = vote.strip().capitalize().replace("  ", " ")
#         if vote not in counts:
#             counts[vote] = 1
#         else:
#             counts[vote] = counts[vote] + 1

# #print("Results:")
# #print()
# for name in counts:
# #    print(name + ": " + str(counts[name]))
    



# with open("radishsurvey.txt") as file:
#     for line in file:
#         line = line.strip()
#         name,vote = line.split(" - ")
#         vote = vote.strip().capitalize().replace("  "," ")
#         if vote not in counts:
#             #first vote for this
#             counts[vote]=1
#         else:
#             #increment the vote
#             counts[vote] = counts[vote]+1
# print(counts)


#Create an empty dictionary for associating radish names
# with vote counts
counts = {}

# Create an empty list with the names of everyone who voted
voted = []

# Clean up (munge) a string so it's easy to match against other     strings
def clean_string(s):
    return s.strip().capitalize().replace("  "," ")

# Check if someone has voted already and return True or False
def has_already_voted(name):
    if name in voted:
        print(name + " has already voted! Fraud!")
        return True
    return False

# Count a vote for the radish variety named 'radish'
def count_vote(radish):
    if not radish in counts:
        # First vote for this variety
        counts[radish] = 1
    else:
        # Increment the radish count
        counts[radish] = counts[radish] + 1


with open("radishsurvey.txt") as file:
    for line in file:
        line = line.strip()
        name, vote = line.split(" - ")
        name = clean_string(name)
        vote = clean_string(vote)
    
        if not has_already_voted(name):
            count_vote(vote)
        voted.append(name)

print("Results:")
print()
for name in counts:
    print(name + ": " + str(counts[name]))


#well now lets try to find the winner
def winner(counts):
    
    winner_name=[]
    
    max_votes=max(counts.values()) #tally the score who has highest
    #max_votes = 72
    for name in counts:#loop through
        if counts[name] >= max_votes:#if the counts are greater than or equal to max votes
            winner_name.append(name)#append the name to the list and then print out the winners
            print("The following have won: ")
            print(winner_name)
        
        
winner(counts)



#%% question 6



#%% question 7
import csv
import geo_distance
import numpy as np
import matplotlib.pyplot as plt

latitudes = {}
longitudes = {}


f = open("airports.dat")
for row in csv.reader(f):
#    if row[3] == "Australia" or row[3] == "Russia":
# print("Country[{}] | Airport[{}] | Latitude & Longitude [{},{}]: ".format(row[3],row[1],row[6],row[7]))
    airport_id = row[4]
    latitudes[airport_id] = float(row[6])
    longitudes[airport_id] = float(row[7])
#    print("Aiport_ID[{}] | Latitude & Long [{},{}]".format(airport_id,latitudes[airport_id],longitudes[airport_id]))

#print(geo_distance.distance(-37.814,144.963,52.519,13.406)) # Melbourne to Berlin in km!
#print(latitudes)
#print(longitudes)

distances = []
f = open("routes.dat")
for row in csv.reader(f):
    source_airport = row[2]
    dest_airport = row[4]
    #print("source airport [{}] and destination airport [{}]".format(source_airport, dest_airport))
#    if source_airport in latitudes:
#        print("*****sourceairport [{}] latitude [{}]".format(source_airport, latitudes[source_airport]))
#    if dest_airport in latitudes:
#        print("*****destairport [{}] latitude [{}]".format(dest_airport, latitudes[dest_airport]))

    if source_airport in latitudes and dest_airport in latitudes:
        source_lat = latitudes[source_airport]
        source_long = longitudes[source_airport]
        dest_lat = latitudes[dest_airport]
        dest_long = longitudes[dest_airport]
        distances.append(geo_distance.distance(source_lat,source_long,dest_lat,dest_long))
        print("source airport: [{}], destination airport: [{}], and distance between(km): [{}]".format(source_airport,dest_airport,geo_distance.distance(source_lat,source_long,dest_lat,dest_long)))

## histogram

plt.hist(distances, 100, facecolor='b')
plt.xlabel("Distance (km)")
plt.ylabel("Number of flights")

