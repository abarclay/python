#!/usr/bin/python

# given a string, print the first character that isn't repeated in the string
# "swiss" would be "w"

mystring="swiss"
hash = {}

for index in range(len(mystring)):
  try:
    val=hash[mystring[index]]
  except:
    val=0
  val=val+1
  hash[mystring[index]] = val

for index in range(len(mystring)):
  #print("checking hash table for " + mystring[index])
  if (hash[mystring[index]] == 1):
    print("first non-repeated: " + mystring[index])
    exit()

