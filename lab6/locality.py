#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:33:42 2022

@author: gavinkoma
"""
# theory to keep in mind:
    
# A[n,n],B[n,n],C[n,n]

# for (i = 0; i < n; i ++):
#     for (j=0;j<n;j++):
#         C[i,j] = 0.0
        
# #matrix multiply
# for (i=0;i<n;n++):
#     for (j=0;j<n;n++):
#         for (k=0;k<n;k++):
#             C[i,j] = C[i,j] + A[i,k] * B[k,j];
            
# rows = 3
# columns = 3

# matrix = []

# for i in range(rows):
#     a = []
#     for j in range(columns):
#         a.append(int())

import numpy as np
import sys
import os
from datetime import datetime
import subprocess
from subprocess import call
from subprocess import check_output

# #matrix size, sort size, number of rep
Nm = int(sys.argv[1])
Ns = int(sys.argv[2])
R = int(sys.argv[3])

#lets check if right
N = 5
x = 0
M1 = np.random.rand(N,N)
M2 = np.random.rand(N,N)

# if (len(sys.argv)<4):
#     print("Usage: script, Nm, Ns, R\n")
#     exit()

#%%
Matrix = [[0 for i in range(N)] for j in range (N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            
w = open('matrixtest-result1','w')
w.write('{}'.format(Matrix))
w.close()


#%%
#round1
x = x + 1

Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for k in range(N):
        for j in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            
w = open('matrixtest-result2','w')
w.write('{}'.format(Matrix))
w.close()

#check difference

out = check_output(["diff","matrixtest-result1",'matrixtest-result2'])
if len(out) != 0:
    print("Difference found in phase" + str(x) + "|" + out + "|")
else:
    print("No difference found in Phase " +str(x))


#%%
#round2
x = x + 1

Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for k in range(N):
        for j in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            
w = open('matrixtest-result2','w')
w.write('{}'.format(Matrix))
w.close()

out = check_output(["diff","matrixtest-result1",'matrixtest-result2'])
if len(out) != 0:
    print("Difference found in phase" + str(x) + "|" + out + "|")
else:
    print("No difference found in Phase " +str(x))


#%%
#round3
x = x + 1

Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for k in range(N):
        for j in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            
w = open('matrixtest-result2','w')
w.write('{}'.format(Matrix))
w.close()

out = check_output(["diff","matrixtest-result1",'matrixtest-result2'])
if len(out) != 0:
    print("Difference found in phase" + str(x) + "|" + out + "|")
else:
    print("No difference found in Phase " +str(x))


#%%
#round4
x = x + 1

Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for k in range(N):
        for j in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            
w = open('matrixtest-result2','w')
w.write('{}'.format(Matrix))
w.close()

out = check_output(["diff","matrixtest-result1",'matrixtest-result2'])
if len(out) != 0:
    print("Difference found in phase" + str(x) + "|" + out + "|")
else:
    print("No difference found in Phase " +str(x))


#%%
#round5
x = x + 1

Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for k in range(N):
        for j in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            
w = open('matrixtest-result2','w')
w.write('{}'.format(Matrix))
w.close()

out = check_output(["diff","matrixtest-result1",'matrixtest-result2'])
if len(out) != 0:
    print("Difference found in phase" + str(x) + "|" + out + "|")
else:
    print("No difference found in Phase " +str(x))


#%%
#round6
x = x + 1

Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for k in range(N):
        for j in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            
w = open('matrixtest-result2','w')
w.write('{}'.format(Matrix))
w.close()

out = check_output(["diff","matrixtest-result1",'matrixtest-result2'])
if len(out) != 0:
    print("Difference found in phase" + str(x) + "|" + out + "|")
else:
    print("No difference found in Phase " +str(x))


#%%performance tests
subprocess.run(["rm", 'matrixtest-result1'])
subprocess.run(["rm", 'matrixtest-result2'])
w = open("matrixtime.txt",'w')

#%%ijk
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#ii/i/g','matrix.c'])
subprocess.run(['sed','-i','s/#jj/j/g','matrix.c'])
subprocess.run(['sed','-i','s/#kk/k/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(N),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
w.write("Matrix i-j-k:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))

#%% do ikj
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#ii/i/g','matrix.c'])
subprocess.run(['sed','-i','s/#kk/k/g','matrix.c'])
subprocess.run(['sed','-i','s/#jj/j/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(N),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
w.write("Matrix i-k-j:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))

#%% do kij
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#kk/k/g','matrix.c'])
subprocess.run(['sed','-i','s/#ii/i/g','matrix.c'])
subprocess.run(['sed','-i','s/#jj/j/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(N),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
w.write("Matrix i-j-k:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))

#%% do jki
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#jj/j/g','matrix.c'])
subprocess.run(['sed','-i','s/#kk/k/g','matrix.c'])
subprocess.run(['sed','-i','s/#ii/i/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(N),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
w.write("Matrix i-j-k:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))


#%% do jik
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#jj/j/g','matrix.c'])
subprocess.run(['sed','-i','s/#ii/i/g','matrix.c'])
subprocess.run(['sed','-i','s/#kk/k/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(N),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
w.write("Matrix i-j-k:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))



