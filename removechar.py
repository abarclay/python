#!/usr/bin/python

# like tr

mystring="baaaaaarrrrraaar"
newstring=""
index=0

while index < len(mystring):
  if (mystring[index]!="a"):
    newstring=newstring + mystring[index]
  index=index+1
print newstring
