#!/usr/local/bin/python3

import sys

print("hello world")

# suppress the newline. python2 only
#print "hello world",
# but that doesn't work with brackets, which I personally like
print ("hello world",)

sys.stdout.write("hello world")

# python 3 only
print ("hello world",end="")
