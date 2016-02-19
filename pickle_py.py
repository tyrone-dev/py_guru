#!/usr/bin/env python

import pickle

# pickle packs python objects into a characterstream - can then unpack this stream in another python script to get the original data

data = pickle.load(open('banner.p', 'rb'))

# need to print a picture using the data from the list in the pickle file

# nicer method
for line in data:
    print ''.join(c*n for c,n in line)

for line in data:
    a = ''
    for element in line:
        a += element[0]*element[1]
    print a
