#!/usr/local/bin/python3

# recursive
def reverse1(mystring):
	if (len(mystring) == 0):
		return("")
	if (len(mystring) == 1):
		return(mystring)
	newstring=reverse1(mystring[1:])+mystring[0]
	return(newstring)

# non-recursive without a lot of adding and subtracting
def reverse2(mystring):
	newstring=""
	for i in range(len(mystring)-1,-1,-1):
		newstring=newstring+mystring[i]
	return(newstring)

print(reverse1("foobar"))
print(reverse2("foobar"))
