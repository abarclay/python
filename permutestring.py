#!/usr/bin/python

# Implementation of Heap's algorithm for permuting objects

def swap(string1,index1,index2):
  #print("called swap with " + string1 + "to swap positions " + str(index1) + str(index2))
  tmp=string1[index2]
  newstring=""
  for i in range(len(string1)):
    if (i == index1):
      newstring=newstring+string1[index2]
      continue
    if (i == index2):
      newstring=newstring+string1[index1]
      continue
    newstring=newstring+string1[i]
  return(newstring)

def generate(k,astring):
  if (k==1):
    print(astring),
  else:
    generate(k-1,astring)

    for i in range(k-1):
      if (k%2 == 0):
      	astring=swap(astring,i,k-1)
      else:
	astring=swap(astring,0,k-1)
      generate(k-1,astring)

# permute a string
mystring="a"
print ("\n\npermuting " + mystring)
generate(len(mystring),mystring)

mystring="ab"
print ("\n\npermuting " + mystring)
generate(len(mystring),mystring)

mystring="abc"
print ("\n\npermuting " + mystring)
generate(len(mystring),mystring)

mystring="abcdef"
print ("\n\npermuting " + mystring)
generate(len(mystring),mystring)
