#!/usr/bin/env python

s = "".join([line.rstrip() for line in open('equality.txt')])

# find small letters with 3 capitial letters on either side i.e. BAGaBAH

answer = ''

def functionHere(index):
    if s[index-3:index].isupper() and s[index+1:index+4].isupper():
        if s[index-4].islower() and s[index+4].islower():
            return True
    else:
        return False

for i in range(len(s)):
    try:
        if s[i].islower(): 
            if functionHere(i):
                answer += s[i] 
    except:
        continue

print answer

# using regex
import re
print "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', s))

