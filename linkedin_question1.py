#!/usr/local/bin/python3

# Write a program which prints out all numbers between 1 and 100. When the program would print out a number exactly divisible by 4, print "Linked" instead. When it would print out a number exactly divisible by 6, print "In" instead. When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn" instead.

# NOTE: my original solution used range(100) which starts at zero
# which isn't really what the question asked.
# The other thing to clarify is whether "between" is inclusive or not
# I assumed it was inclusive and let the interviewer know that

for index in range(1,101):
    if ((index % 4) == 0) and ((index % 6) == 0):
        print("LinkedIn")
    else:
        if ((index % 4) == 0):
            print("Linked")
        else:
            if ((index % 6) == 0):
                print("In")
            else:
                print(index)
                
# after completing this, the interviewer asked me why I chose nested
# if statements.
# python doesn't have a case statement - but there are ways to implement them
