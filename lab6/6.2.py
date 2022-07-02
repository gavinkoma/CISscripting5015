#!/home/TU/shi/anaconda3/bin/python

#Given a C square matrix multiplication program, compose a Python 
#All six different (i,j,k) loop orders will generate the identical outputs
#Find the order that delivers the best performance
#Demonstrate the scaling effects of the fastest order by running n in range(100,5000,100)
#Project the power chart by plotting W=Telapsed/(n3) against n 
#Set n=3, hand draw six data access patterns for the six i-j-k orders. Explain why the fastest order?

#Code from Panopto Recordings: "June 28, 2022(Lab6.1 Debugging + Lab6.2 Scalability Plot)"

import numpy as np
import random
import sys
import os
from datetime import datetime
import string
import subprocess
from subprocess import call
from subprocess import check_output

if (len(sys.argv) < 3):
	print("Usage: test script Nm R\n")
	exit()

Nm = int(sys.argv[1]) #Matrix size
R = int(sys.argv[2]) #Number of repetitions
	
#Order correctness test
N = 5 #For correctness tests only
x = 0 #For phase count
M1 = np.random.rand(N, N)
M2 = np.random.rand(N, N)
Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
	for j in range(N):
		for k in range(N):
			Matrix[i][j] += M1[i][k] * M2[k][j]
			
w = open("MTResult-1.txt", "w")
w.write("{}".format(Matrix))
w.close()

x = x+1
Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
	for k in range(N):
		for j in range(N):
			Matrix[i][j] += M1[i][k] * M2[k][j]
			
w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = check_output(["diff", "MTResult-1.txt", "MTResult-2.txt"])
if len(out) != 0:
	print("No difference found in Phase " + str(x)) + "|" + out + "|"
else:
	print("No difference found in Phase " + str(x))

x = x+1
Matrix = [[0 for i in range(N)] for j in range(N)]

for j in range(N):
	for k in range(N):
		for i in range(N):
			Matrix[i][j] += M1[i][k] * M2[k][j] #line 59
			
w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = check_output(["diff", "MTResult-1.txt", "MTResult-2.txt"])
if len(out) != 0:
	print("No difference found in Phase " + str(x)) + "|" + out + "|"
else:
	print("No difference found in Phase " + str(x))

x = x+1
Matrix = [[0 for i in range(N)] for j in range(N)]
	
for j in range(N):
	for i in range(N):
		for k in range(N):
			Matrix[i][j] += M1[i][k] * M2[k][j] #line 76
			
w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = check_output(["diff", "MTResult-1.txt", "MTResult-2.txt"])
if len(out) != 0:
	print("No difference found in Phase " + str(x)) + "|" + out + "|"
else:
	print("No difference found in Phase " + str(x))
	
x = x+1
Matrix = [[0 for i in range(N)] for j in range(N)]
	
for k in range(N):
	for i in range(N):
		for j in range(N):
			Matrix[i][j] += M1[i][k] * M2[k][j] #line 93
			
w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = check_output(["diff", "MTResult-1.txt", "MTResult-2.txt"])
if len(out) != 0:
	print("No difference found in Phase " + str(x)) + "|" + out + "|"
else:
	print("No difference found in Phase " + str(x))
	
x = x+1
Matrix = [[0 for i in range(N)] for j in range(N)]
	
for k in range(N):
	for j in range(N):
		for i in range(N):
			Matrix[i][j] += M1[i][k] * M2[k][j] #line 110
			
w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = check_output(["diff", "MTResult-1.txt", "MTResult-2.txt"])
if len(out) != 0:
	print("No difference found in Phase " + str(x)) + "|" + out + "|"
else:
	print("No difference found in Phase " + str(x))
	
#Matrix Performance Tests
subprocess.run(["rm", "MTResults-1.txt"]) #clean up all text files
subprocess.run(["rm", "MTResults-2.txt"]) #clean up all text files

w = open("MTime.txt", "w") #open MTime.txt log files

#ijk
subprocess.run(["cp", "template.c", "matrix.c"])
subprocess.run(["sed", "-i", "s/#1/i/g", "matrix.c"]) #line 131
subprocess.run(["sed", "-i", "s/#2/j/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#3/k/g", "matrix.c"])
subprocess.run(["gcc", "-DN="+str(Nm),"-o", "matrix", "matrix.c"])
Te = datetime.now()
for i in range(R):
	subprocess.run(["./matrix"])
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
w.write("Matrix i-k-j:\n {N} {T} {M}\n".format(N=Nm, T=TotalUS, M=pow(Nm,3)/TotalUS))

#jik
subprocess.run(["cp", "template.c", "matrix.c"])
subprocess.run(["sed", "-i", "s/#1/j/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#2/i/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#3/k/g", "matrix.c"])
subprocess.run(["gcc", "-DN="+str(Nm),"-o", "matrix", "matrix.c"])
Te = datetime.now()
for i in range(R):
	subprocess.run(["./matrix"])
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
w.write("Matrix j-i-k:\n {N} {T} {M}\n".format(N=Nm, T=TotalUS, M=pow(Nm,3)/TotalUS))

#jki
subprocess.run(["cp", "template.c", "matrix.c"])
subprocess.run(["sed", "-i", "s/#1/j/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#2/k/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#3/i/g", "matrix.c"])
subprocess.run(["gcc", "-DN="+str(Nm),"-o", "matrix", "matrix.c"])
Te = datetime.now()
for i in range(R):
	subprocess.run(["./matrix"])
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
w.write("Matrix j-k-i:\n {N} {T} {M}\n".format(N=Nm, T=TotalUS, M=pow(Nm,3)/TotalUS)) #line 140

#ikj
subprocess.run(["cp", "template.c", "matrix.c"])
subprocess.run(["sed", "-i", "s/#1/i/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#2/k/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#3/j/g", "matrix.c"])
subprocess.run(["gcc", "-DN="+str(Nm),"-o", "matrix", "matrix.c"])
Te = datetime.now()
for i in range(R):
	subprocess.run(["./matrix"])
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
w.write("Matrix i-k-j:\n {N} {T} {M}\n".format(N=Nm, T=TotalUS, M=pow(Nm,3)/TotalUS))

#jik
subprocess.run(["cp", "template.c", "matrix.c"])
subprocess.run(["sed", "-i", "s/#1/j/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#2/i/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#3/k/g", "matrix.c"])
subprocess.run(["gcc", "-DN="+str(Nm),"-o", "matrix", "matrix.c"])
Te = datetime.now()
for i in range(R):
	subprocess.run(["./matrix"])
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
w.write("Matrix j-i-k:\n {N} {T} {M}\n".format(N=Nm, T=TotalUS, M=pow(Nm,3)/TotalUS)) #line 166

#jki    line 168
subprocess.run(["cp", "template.c", "matrix.c"])
subprocess.run(["sed", "-i", "s/#1/j/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#2/k/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#3/i/g", "matrix.c"])
subprocess.run(["gcc", "-DN="+str(Nm),"-o", "matrix", "matrix.c"])
Te = datetime.now()
for i in range(R):
	subprocess.run(["./matrix"])
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
w.write("Matrix j-k-i:\n {N} {T} {M}\n".format(N=Nm, T=TotalUS, M=pow(Nm,3)/TotalUS))

#kij
subprocess.run(["cp", "template.c", "matrix.c"])
subprocess.run(["sed", "-i", "s/#1/k/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#2/i/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#3/j/g", "matrix.c"])
subprocess.run(["gcc", "-DN="+str(Nm),"-o", "matrix", "matrix.c"])
Te = datetime.now()
for i in range(R):
	subprocess.run(["./matrix"])
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
w.write("Matrix k-i-j:\n {N} {T} {M}\n".format(N=Nm, T=TotalUS, M=pow(Nm,3)/TotalUS))

#kji
subprocess.run(["cp", "template.c", "matrix.c"])
subprocess.run(["sed", "-i", "s/#1/k/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#2/j/g", "matrix.c"])
subprocess.run(["sed", "-i", "s/#3/i/g", "matrix.c"])
subprocess.run(["gcc", "-DN="+str(Nm),"-o", "matrix", "matrix.c"])
Te = datetime.now()
for i in range(R):
	subprocess.run(["./matrix"])
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
w.write("Matrix k-j-i:\n {N} {T} {M}\n".format(N=Nm, T=TotalUS, M=pow(Nm,3)/TotalUS))

w2 = open("ScalabilityTest.dat", "w")
for i in range(100, 5000, 100):
	subprocess.run(["cp", "template.c", "matrix.c"])
	subprocess.run(["sed", "-i", "s/#1/i/g", "matrix.c"])
	subprocess.run(["sed", "-i", "s/#2/k/g", "matrix.c"])
	subprocess.run(["sed", "-i", "s/#3/j/g", "matrix.c"])
	subprocess.run(["gcc", "-DN="+str(i),"-o", "matrix", "matrix.c"])
	Te = datetime.now()
	subprocess.run(["./matrix"])
	Te = datetime.now() - Te
	TotalUS = float((Te.seconds * 1000000 + Te.microseconds))
	w2.write("New_Matrix i-k-j:\n {N} {T} {M}\n".format(N=i, T=TotalUS, M=pow(Nm,3)/TotalUS))
w2.close()

M1 = np.random.rand(Nm, Nm)
M2 = np.random.rand(Nm, Nm)
Te = datetime.now()
for i in range(R):
	Result = np.dot(M1, M2)
Te = datetime.now() - Te
TotalUS = float((Te.seconds * 1000000 + Te.microseconds)/R)
Mflops = pow(Nm, 3) / TotalUS

w.write("numpy Results: \n {N} {T} {M} \n".format(N=Nm, T=TotalUS, M=Mflops))
