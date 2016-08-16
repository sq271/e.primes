#!/bin/python

# cleanup.py <filename>

# rm numbers with a leading zero

import sys

fname = sys.argv[1]

with open(fname,'r') as input:
    with open('new'+ fname,'w') as output:
        for line in input:
            if line in ('0\n','1\n'):
                pass
            elif line[0] == '0':
                pass
            else:
                output.write(line)
