#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 18:10:22 2022

@author: gavinkoma
"""

import random
from collections import defaultdict
from collections import Counter
import operator

#%%q5
string = "gc"

add1 = '1'

stuff = "{}{}".format(string,add1)

print(stuff)

#%%q7

dnaIn = open("dna1.dat")
contents = dnaIn.read()
dnaIn.close()

counte = contents.count("CG")
print(counte)