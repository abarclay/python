#!/usr/bin/python3

# add 100 integers to a list - except skip one
# find out which one is missing

mylist=[]
for i in range(100):
    if(i!=69):
        mylist.append(i)

# now, let's find the one that is missing
for i in range(100):
    try:
        any=mylist.index(i)
    except:
        print("The missing integer is: " + str(i))