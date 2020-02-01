#!/usr/bin/python

def isPalindrome(mystring):
  l=len(mystring)
  # assume a zero length string is not a palindrome
  if (l == 0):
    return(false)
  index=0
  palindrome=true
  while (index <= l/2):
    if (mystring[index] != mystring[l-1-index]):
      palindrome=false
    index=index+1

  return(palindrome)

# main
true=0
false=1
mystring="this is a test"
mystring="this siht test"
mystring="funny this siht test"
palindromes=[]
longest=""

for i in range(len(mystring)):
  for j in range(len(mystring)):
    teststring=mystring[i:i+j+1]
    #print teststring
    if (isPalindrome(teststring) == true):
      palindromes.append(teststring)
      if (len(teststring) > len(longest)):
	longest=teststring

print("longest: " + longest)
