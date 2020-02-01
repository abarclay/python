#!/usr/bin/python

# given an array of numbers, find any duplicates

# originally, I was thinking of just sorting, then walking through
# but I think perhaps a hash table would be better

numbers = [ 3, 4, 5, 6, 1, 2, 3, 9 ]

hash = {}

for num in numbers:
  try:
    val=hash[num]
  except:
    val=0
  val=val+1
  hash[num] = val

for num in hash:
  if (hash[num] > 1):
    print("duplicates: " + str(num))

