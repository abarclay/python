#!/usr/local/bin/python3

import re
n = int(input())
for i in range(n):
    line=input()
    line = re.sub(" && ", " and ",line)
    line = re.sub(" \|\| ", " or ", line)
    print(line)
