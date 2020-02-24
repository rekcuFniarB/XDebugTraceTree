#!/usr/bin/env python3

##  xdebugtracetree - add trees to xdebug traces.
##  Copyright (C) 2019  BrainFucker <retratserif@gmail.com>
##  
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##  
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.

import sys

## Input lines
lines = None
## Output lines
output = []

if (len(sys.argv) < 2):
    sys.stderr.write('Usage: %s "xdebug_trace.xt"\n' % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    lines = f.readlines()

## Previous function position
prevpos = 0
fork = None
forks = []

def storeFork(position):
    if position > 0 and position not in forks:
            forks.append(position)

def removeFork(position):
        if position in forks:
            forks.remove(position)

for line in reversed(lines):
    line = line.decode('utf-8', 'replace')
    ## Current position
    position = line.find('->')
    storeFork(position)
    
    ## working with string as array
    _line = list(line)
    for fork in forks:
        ## close forks if current element is higher in hiearchy
        if fork > position:
            removeFork(fork)
        
        if fork < position:
            ## put fork mark at every stored position
            _line[fork] = '│'
        
    line = ''.join(_line)
        
    ## store line for output
    output.insert(0, line.replace(' ->', ' └>'))
    
    ## remember previous position
    prevpos = position
    ## end for

for line in output:
    sys.stdout.write(line)

