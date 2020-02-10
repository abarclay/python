#!/usr/local/bin/python3

# function will return true if two strings are an anagram of each other

# lots of ways to do this
# easiest is to sort both strings, then walk though and compare each char

def sort(mystring):
    mylist = []
    newstring=""
    for i in range(len(mystring)):
        mylist.append(mystring[i])
    mylist.sort()
    for i in range(len(mystring)):
        newstring=newstring + mylist[i]
    return(newstring)

def isAnagram(string1,string2):
    if (len(string1) != len(string2)):
        return(false)
    sortedString1=sort(string1)
    sortedString2=sort(string2)
    for i in range(len(sortedString1)):
        if (sortedString1[i] != sortedString2[i]):
            return(false)
    return(true)        


false=0
true=1

string1="foobar"
string2="bard"

string1="foobar"
string2="barfoo"

string1="foobar"
string2="badfoo"

if isAnagram(string1,string2):
    print("the two strings are anagrams: " + string1 + " " + string2)
else:
    print("the two strings are NOT anagrams: " + string1 + " " + string2)