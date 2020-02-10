#!/usr/local/bin/python3

# remove any duplicate values in the array

def removeDups(mylist):
    myhash = {}

    for i in range(len(mylist)):
        myhash[mylist[i]] = 0;
    return(list(myhash))

# main
alist = [ 1, 2, 3, 4, -3, 5, 3, 6, 7, 9, 10, 9]
print(removeDups(alist))