#!/usr/local/bin/python3

# We are building a word processor and we would like to implement a "reflow" functionality that also applies full justification to the text.

# Given an array containing lines of text and a new maximum width, re-flow the text to fit the new width. Each line should have the exact specified width. If any line is too short, insert '-' (as stand-ins for spaces) between words as equally as possible until it fits.

# Note: we are using '-' instead of spaces between words to make testing and visual verification of the results easier.

lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]

# reflowAndJustify(lines, 24) ... "reflow lines and justify to length 24" =>

#         [ "The--day--began-as-still",
#           "as--the--night--abruptly",
#           "lighted--with--brilliant",
#           "flame" ] // <--- a single word on a line is not padded with spaces

# reflowAndJustify(lines, 26) ... "reflow lines and justify to length 26" =>

#         [ "The--day-began-as-still-as",
#           "the-night-abruptly-lighted",
#           "with----brilliant----flame" ]

# reflowAndJustify(lines, 40) ... "reflow lines and justify to length 40" =>

#         [ "The--day--began--as--still--as-the-night",
#           "abruptly--lighted--with--brilliant-flame" ]

# n = number of words OR total characters

import re

def wordwrap(mylist,maxlength):
    newlist=[]
    currlength=0
    newline=""
    for word in mylist:
        #print(word)
        if (newline == ""):
            newlength=len(word)
        else:
            newlength=len(word)+ 1
        if ((currlength + newlength) <= maxlength):
            if (newline == ""):
                currlength=currlength + len(word)
                newline=word
            else:
                currlength=currlength + len(word) + 1
                newline=newline + "-" + word
        else:
            newlist.append(newline)
            newline=word
            currlength=len(word)
    newlist.append(newline)
    return(newlist)

def expand1(mystring,maxlength):
	#print(mystring)
	# there are are no dashes, just return
	if ("-" not in mystring):
		return(mystring)
	#how many - do we need to add?
	num=maxlength-len(mystring)
	index=0
	newstring=""
	while (num > 0):
		#print(newstring)
		newstring=newstring + mystring[index]
		if (mystring[index] == "-"):
			# add a -
			newstring=newstring + "-"
			num=num-1
			index=index+1
			# fast forward to next non "-"
			while ((index < len(mystring)) and (mystring[index] == "-")):
				newstring=newstring+mystring[index]
				index=index + 1
		else:
			index=index+1
		# if we are at the end of the string, start at beginning again
		if ((index == len(mystring)) and (num > 0)):
			index=0
			mystring=newstring
			newstring=""
	return(newstring)

def expand(mystring,maxlength):
	# if there are no dashes in the string, just return the string
	if ("-" not in mystring):
		return(mystring)

	# lets be smart about this
	# how many - do I need to add
	tot=maxlength-len(mystring)

	# and how many groups of "-" are there in the string
	count=mystring.count("-")
	dashesToAdd,extraOneForThese=divmod(tot,count)
	#print("need to add " + str(dashesToAdd) + "to each of the " + str(count))
	#print("need to add one extra for each of the first " + str(extraOneForThese))
	repdash="-"
	for i in range(dashesToAdd):
		repdash=repdash+"-"
	if (dashesToAdd > 0):
		mystring=re.sub("-",repdash,mystring,0)
	if (extraOneForThese > 0):
		mystring=re.sub("-","--",mystring,extraOneForThese)
	return(mystring)

def reflowAndJustify(mylist,maxlength):
    newlist=[]
    currlength=0
    newline=""
    for phrase in mylist:
        newphrase=phrase.split()
        for word in newphrase:
            #print(word)
            if (newline == ""):
                newlength=len(word)
            else:
                newlength=len(word)+ 1
            if ((currlength + newlength) <= maxlength):
                if (newline == ""):
                    currlength=currlength + len(word)
                    newline=word
                else:
                    currlength=currlength + len(word) + 1
                    newline=newline + "-" + word
            else:
                newline=expand(newline,maxlength)
                newlist.append(newline)
                newline=word
                currlength=len(word)
    newline=expand(newline,maxlength)
    newlist.append(newline)

    return(newlist)

print (reflowAndJustify(lines,24))
print (reflowAndJustify(lines,26))
print (reflowAndJustify(lines,40))
