#!/usr/local/bin/python3

#Given an array of ints,
#return the smallest positive integer that doesn't appear in the list

#A = [ 1, 13, 3, 4, 7 ]
A = [ 1, 2, 3 ]
#A = [ -1, -3 ]
#A = [ 1, 3, 6, 4, 1, 2 ]

A.sort()
i=1
false=0
true=1

while (i <= len(A)+1):
	found=false
	for val in A:
		if(i==val):
			found=true
	if (found == false):
		print(i)
	i = i + 1

