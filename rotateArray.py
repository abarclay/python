#!/usr/local/bin/python3

def rotate(myArray):
    if (len(myArray) == 0):
        return()
    tmp=myArray[len(myArray)-1]
    index = len(myArray) - 1
    while (index > 0):
        #print("copying index " + str(index))
        myArray[index] = myArray[index-1]
        index = index - 1
    myArray[0]=tmp

def solution(A, K):
    for i in range(K):
        rotate(A)
    return(A)


A=[3,8,9,7,6]
out=solution(A,3)
print(out)
