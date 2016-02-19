#!/usr/bin/env python

# need to generate the look and say sequnce
# - read the previous number's number of appearnaces and value 
# to get the next number in the sequnce
# i.e. 1 - {one one} so the next number is 11 - {two one's} so the next is
# 21 -{one two, one one} to the next number is 1211 etc.

import itertools


#a = [1, 11, 21, 1211, 111221]
#a = map(str, a)

look_and_say_sequence = [1]

def get_next_number(prev_num):
    new_number = ""
    #groups = []
    #for k, g in itertools.groupby(prev_num):
    #    groups.append(list(g)
    
    # list comprehension coz yes
    groups = [list(g) for k, g in itertools.groupby(prev_num)]
    for group in groups:
        new_number += str(len(group)) + group[0]

    return new_number

for i in range(10):
    look_and_say_sequence.append(int(get_next_number(str(look_and_say_sequence[i]))))

print look_and_say_sequence
