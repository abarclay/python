#!/usr/bin/python

def square(myint):
  return(myint * myint)

#main
mylist=[-3,1,4,18]
newlist=[]

print "Initial list: ", mylist
for i in mylist:
  newlist.append(square(i))
print "Squared list: ", newlist
newlist.sort()
print "Sorted Squared list: ", newlist
