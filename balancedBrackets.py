#!/usr/bin/python

import re

#"Some String" true
#"]Some String" false
#"This [ is a string {that contains} () a balanced set]. It is good" true

#main

true=0
false=1
mystring="Some String" # true
mystring="Som[[e] String" #false
mystring="This [ is a <string<>> {that contains} () a balanced set]. It is good" #true
balcharsregex="[[]{}()<>]"
openbrackets="[[{(<]"
closebrackets="[\]})>]"
openbracketsregex=re.compile(openbrackets)
closebracketsregex=re.compile(closebrackets)
stack=[]
index=0
balanced=true

while (index < len(mystring)):
  if (openbracketsregex.match(mystring[index])):
    stack.append(mystring[index])

  if (closebracketsregex.match(mystring[index])):
    try:
      lastbracket=stack.pop()
      #print mystring[index]
      #print lastbracket
    except:
      balanced=false
    if (((mystring[index] == "]") and (lastbracket == "[")) or
        ((mystring[index] == "}") and (lastbracket == "{")) or
        ((mystring[index] == ")") and (lastbracket == "(")) or
        ((mystring[index] == ">") and (lastbracket == "<"))):
      #print "good"
      nothing=0
    else:
      balanced=false
  index=index+1

if ((balanced==false) or (len(stack) > 0)):
  print "not balanced"
else:
  print "balanced"

