#!/usr/local/bin/python3

# given an array, find the second largest number in the array

mylist = [ 1, -3, 13, 27, 100, 103, 18]

mylist.sort()

print(mylist[len(mylist)-2])