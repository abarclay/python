#!/usr/local/bin/python3
# function that returns 1 if the passed Array is a permutation and
# 0 otherwise

def solution(A):
    A.sort()
    for i in range(len(A)):
        if (A[i] != i+1):
            return(0)
    return(1)
