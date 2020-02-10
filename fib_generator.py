#!/usr/local/bin/python3

# fill in this function
def fib():
    a=1
    b=1
    yield a
    yield b
    while (0 == 0):
        c=a+b
        yield c
        a=b
        b=c

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
