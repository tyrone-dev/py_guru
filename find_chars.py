#!/usr/bin/env python

# open text file

import string

ascii_letters = string.ascii_letters

f = open('random_char.txt', 'rb')

rare_chars = ''

# my method: look for alpha characters - assumption!

garbage = f.read()

for char in garbage:
    if char in ascii_letters:
        rare_chars += char

print rare_chars

# less code, same idea

print "".join([char for char in garbage if char.isalpha()])

# finding rare chars based on less frequent appearance

s = "".join([line.rstrip() for line in open('random_char.txt')])
OCCURANCES = {} # dict
for c in s: OCCURANCES[c] = OCCURANCES.get(c,0) + 1
avgOC = len(s) / len(OCCURANCES)

print "".join([c for c in s if OCCURANCES[c] < avgOC])
