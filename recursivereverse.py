#!/usr/bin/python

# reverse a string using recursion

def reverse(mystring):
  if (len(mystring) <= 1):
    return(mystring[0])
  else:
    revstring=reverse(mystring[1:len(mystring)]) + mystring[0]
  return(revstring)

# main
true=0
false=1
x=reverse("1234567")
print x
