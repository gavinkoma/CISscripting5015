#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:43:08 2022

@author: gavinkoma
"""

import pandas as pd

matrix = pd.read_excel("matrixtimes.xlsx", header = 0, index_col = None)

df = pd.DataFrame({'ijk':pd.Series(matrix.iloc[1,1:])}); 
df['ikj'] = pd.Series(matrix.iloc[3,1:])
df['kij'] = pd.Series(matrix.iloc[5,1:])
df['kji'] = pd.Series(matrix.iloc[7,1:])
df['jki'] = pd.Series(matrix.iloc[9,1:])
df['jik'] = pd.Series(matrix.iloc[11,1:])


#graph 
df['ijk']=df['ijk'].astype(float)
df['ikj']=df['ikj'].astype(float)
df['kij']=df['kij'].astype(float)
df['kji']=df['kji'].astype(float)
df.plot()
