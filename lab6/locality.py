#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:33:42 2022

@author: gavinkoma
"""
import numpy as np
import sys
from datetime import datetime
import subprocess
from subprocess import check_output
from xlwt import Workbook
import xlsxwriter
import csv

# #matrix size, number of rep
if (len(sys.argv) < 2):
    print("Usage: locality matrixSize repetition\n")
    exit()
Nm = int(sys.argv[1])
R = int(sys.argv[2])

#lets check if right
N = 5
x = 0
M1 = np.random.rand(N,N)
M2 = np.random.rand(N,N)

# if (len(sys.argv)<4):
#     print("Usage: script, Nm, Ns, R\n")
#     exit()

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

subprocess.run(['gcc','-DN='+str(Nm),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
#w.write("Matrix i-j-k:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))
w.write("Matrix i-j-k:\n {T}\n".format(T=TotalUs))

#%% do ikj
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#ii/i/g','matrix.c'])
subprocess.run(['sed','-i','s/#jj/k/g','matrix.c'])
subprocess.run(['sed','-i','s/#kk/j/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(Nm),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
# w.write("Matrix i-k-j:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))
w.write("Matrix i-k-j:\n {T}\n".format(T=TotalUs))
#%% do kij
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#ii/k/g','matrix.c'])
subprocess.run(['sed','-i','s/#jj/i/g','matrix.c'])
subprocess.run(['sed','-i','s/#kk/j/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(Nm),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
# w.write("Matrix k-i-j:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))
w.write("Matrix k-i-j:\n {T}\n".format(T=TotalUs))
#%% do kji
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#ii/k/g','matrix.c'])
subprocess.run(['sed','-i','s/#jj/j/g','matrix.c'])
subprocess.run(['sed','-i','s/#kk/i/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(Nm),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
# w.write("Matrix k-j-i:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))
w.write("Matrix k-j-i:\n {T}\n".format(T=TotalUs))
#%% do jki
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#ii/j/g','matrix.c'])
subprocess.run(['sed','-i','s/#jj/k/g','matrix.c'])
subprocess.run(['sed','-i','s/#kk/i/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(Nm),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
# w.write("Matrix j-k-i:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))
w.write("Matrix j-k-i:\n {T}\n".format(T=TotalUs))

#%% do jik
subprocess.run(['cp','template.c','matrix.c'])
subprocess.run(['sed','-i','s/#ii/j/g','matrix.c'])
subprocess.run(['sed','-i','s/#jj/i/g','matrix.c'])
subprocess.run(['sed','-i','s/#kk/k/g','matrix.c'])

subprocess.run(['gcc','-DN='+str(Nm),'-o','Matrix','matrix.c'])

Te = datetime.now()
for i in range(R):
    subprocess.run(['./Matrix'])
Te = datetime.now() - Te
TotalUs = float((Te.seconds*1000000+Te.microseconds)/R)
# w.write("Matrix j-i-k:\n {N} {T} {M}\n".format(N=Nm, T=TotalUs, M=pow(Nm,3)/TotalUs))
w.write("Matrix j-i-k:\n {T}\n".format(T=TotalUs))


#%% do the fastest one
w2 = open("ScalabilityTest.csv", "w")

header=['Order','Time','MFLOPS']
f = open('Data1.csv', 'w')
writer = csv.writer(f)


for i in range(100, 5000, 100):
	subprocess.run(["cp", "template.c", "matrix.c"])
	subprocess.run(["sed", "-i", "s/#ii/i/g", "matrix.c"])
	subprocess.run(["sed", "-i", "s/#jj/k/g", "matrix.c"])
	subprocess.run(["sed", "-i", "s/#kk/j/g", "matrix.c"])
	subprocess.run(["gcc", "-DN="+str(i),"-o", "Matrix", "matrix.c"])
	Te = datetime.now()
	subprocess.run(["./Matrix"])
	Te = datetime.now() - Te
	TotalUS = float((Te.seconds * 1000000 + Te.microseconds))
	w2.write("New_Matrix i-k-j:\n {N}, {T}, {M}\n".format(N=i, T=TotalUS, M=pow(Nm,3)/TotalUS))
w2.close()

M1 = np.random.rand(Nm, Nm)
M2 = np.random.rand(Nm, Nm)
Te = datetime.now()
for i in range(R):
	Result = np.dot(M1, M2)
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
Mflops = pow(Nm, 3) / TotalUS



