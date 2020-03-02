#!/usr/local/bin/python3

import numpy

numpy.set_printoptions(legacy='1.13')
n=int(input())
A=[]
for i in range(n):
    A.append(list(map(float,input().split())))
print(numpy.linalg.det(A))
