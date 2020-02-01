#!/usr/local/bin/python3

def ispalindrome(mystring):
  l=len(mystring)
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
x=ispalindrome("foof")
x=ispalindrome("fool")
#x=ispalindrome("lol")
#x=ispalindrome("12344321")
if (x==true):
  print("true")
else:
  print("false")
