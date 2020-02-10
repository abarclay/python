#!/usr/local/bin/python3

# given an array, find all the numbers in the array that sum to a given number

sum=6
mylist = [ 1, 2, 3, 4, -3, 5, 6, 7, 9]

i=0
while (i < len(mylist)-1):
    j=i+1
    while (j < len(mylist)):
        #print("checking " + str(mylist[i]) + " " + str(mylist[j]))
        if (mylist[i] + mylist[j] == sum):
            print(mylist[i], mylist[j])
        j=j+1
    i=i+1