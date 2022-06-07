#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:37:54 2022

@author: gavinkoma
"""
import random
#%% random module

print(random.randint(0,5)) #random interger from 0-5
print(random.choice("ACGT")) #random selection form acgt
print(random.choices([20,30,40,50],k=2)) #random selection of 2 from a list

#for char in contents:
    #do the work here for each "char" as a member in contents
    
# "separator".join(tuple)()
# cnt = string.count("str") #count str occurances in string
# rs = reversed(string)
# list[::-1] (reverses list)
# enumerate(array) = [(0,e1),(1,e2),(2,e3)]
# zip(str1,str2) = ((ee1,ee21),(e12,e22),...)

#example: generate 10m000 random DNA bases #question #4?
#" ".join([random.choice('ACGT') for _ in range(10000)])




#%% question1

dnaIn = open("dna1.dat")
contents = dnaIn.read()
dnaIn.close()

#pattern search:
    #find number of occurences of pattern in contents
    
#count total number of DNA bases and totals for ACGT
countacgt = contents.count("ACGT")
counta = contents.count("A")
countc = contents.count("C")
countg = contents.count("G")
countt = contents.count("T")

with open("dna1-baseCount.txt",'w') as f:
    f.write('Base Pair count: ' + str(countacgt) + '\n')
    f.write('Total Adenine Count (A): ' + str(counta) + '\n')
    f.write('Total Cytosine Count (C): ' + str(countc) + '\n')
    f.write('Total Guanine Count (G): ' + str(countg) + '\n')
    f.write('Total Thymine Count (T) ' + str(countt) + '\n')
    

#%%question2
#calculate occurrences of ATGTTG in dn1.dat
countatgttg = contents.count("ATGTTG")
with open("dna1-patternCount.txt",'w') as f:
    f.write('\n\n' + 'Occurrences of "ATGTTG": ' + str(countatgttg))
    
    
#%%question3
#(2 pts) The double counter-rotating helix structure of DNA allows 
#sequencing a single strand and derive the reverse complement for the 
#pairing strand. Given DNA ‘GTCCGTCCGAGGGAAATTGCGCATTCTGG’, its reverse 
#complement is rev(‘CAGGCAGGCTCCCTTTAACGCGTAAGACC’). The complement 
#rules are {‘A’:’T’, ‘C’:’G’, ‘G’:’C’, ‘T’:’A’}. Compose a Python program 
#to compute the reverse complement of file “dna1.dat”. Save your output to 
#“dna1-revComplement.txt”. (Hint: use extended slicing L[::-1] for reverse 
#the list of L) 

#smalldna = "GTCCGTCCGAGGGAAATTGCGCATTCTGG"
#print(smalldna)

contents = contents.replace('\n',"")
contents = contents.replace('\t',"")

smalldna = str(contents)

def reverseddna(smalldna):
    complement = {'A':'T','C':'G','G':'C','T':'A'}
    rc = ''.join([complement[base] for base in smalldna[::-1]])
   # print(rc)
    return rc

#print("reversed complement: " + str(reverseddna(smalldna)))

rc = reverseddna(smalldna)

with open("dna1-revComplement.txt","w") as f:
    f.write("The reversed complement of the provided DNA is: " + '\n' 
            + str(rc))

#bases = [complement[base] for base in bases][::-1]



#%% question 4
#compose a program to generate a random DNA sequence with 10,000 bases
#save your output to "dnaOut.txt" ((use random.choice and range functions))

#example: generate 10000 random DNA bases #question #4?

choice = ''.join([random.choice('ACGT') for dna in range(10000)])

with open("dnaOut.txt",'w') as f:
    f.write("A randomly generated DNA sequence of 10000 bases:\n" + str(choice))
    
    
    
#%% question 5
#DNA with low GC-content is less stable than DNA with high GC-content. 
#It is generally believed that GC content plays a necessary role in 
#adaptation temperatures. Compose a Python program to determine the 
#percentage of “GC” contents (G+C/(A+T+G+C)) in “dna1.dat”. Save your output
#to “dna1-gcCount.txt”. (Hint: Build a gc-string then compare, or count g + 
#count c then compare)

#values were just taken from earlier counts
gval = countg
cval = countc
tval = countt
aval = counta

gval,cval = int(countg),int(countc)
tval,aval = int(countt),int(counta)

gctot = gval+cval
acgttot = gval+cval+tval+aval
gv_percent = gctot/acgttot
print(gv_percent)

with open("dna1-gcCount.txt",'w') as f:
    f.write('Total Adenine Count (A): ' + str(counta) + '\n')
    f.write('Total Cytosine Count (C): ' + str(countc) + '\n')
    f.write('Total Guanine Count (G): ' + str(countg) + '\n')
    f.write('Total Thymine Count (T): ' + str(countt) + '\n\n')
    f.write('Total "GC" Count (GC): ' + str(gctot) + '\n')
    f.write('Total Base Count (ACGT): ' + str(acgttot) +'\n')
    f.write('Percent of "GC" content in DNA1: ' + str(gv_percent))
    

#%%question 6
#Given two DNA sequences of equal length, the hamming distance is the 
#number of mismatching characters. For example, the hamming distance between 
#‘TCCGA’ and ‘CTGGA’ is 3. The Hamming distance between two DNA sequences 
#plays a role in DNA molecular recognition. Compose a Python program to 
#calculate the hamming distance between “dna1.dat” and “dna2.dat”. Save your 
#output to “hammingOut.txt”. (Hint: Consider use “set.difference” to shorten 
#your code)

dna1_content = open("dna1.dat")
dna1 = dna1_content.read()
dna1_content.close()

dna2_content = open('dna2.dat')
dna2 = dna2_content.read()
dna2_content.close()

# dna1 = 'TCCGA'
# dna2 = 'CTGGA'

#we want to loop through this probably
#and up the count as we compare

countval = 0

if len(dna1) != len(dna2):
    print("DNA strands not the same length~")
else:
    for index,(i,j) in enumerate(zip(dna1,dna2)):
        if i!=j:
            countval+=1
    print(countval)

with open("hammingOut.txt",'w') as f:
    f.write('Total Hamming Distance: ' + str(countval) + '\n')

    
#%%question 7
#In genetics, a sequence motif is a nucleotide or amino-acid sequence 
#pattern that is wide-spread and has or is conjectured to have a biological 
#significance. Compose a Python program to find the top 5 most frequent k=5 
#motifs in dna1.dat. Order your output and save it to “Top5Motifs.txt”.


k = 5
dna = 'GTCCGTCGAGGGAAATTGCGCATTCTGG'
for i in range(len(dna) - k +1):
    print(dna[i:i+k])







