#!/usr/local/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt="%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1,fmt)
    time2 = datetime.strptime(t2,fmt)
    print(time1)
    print(time2)
    diff=time1-time2
    return(str(abs(diff.days*86400 + diff.seconds)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

