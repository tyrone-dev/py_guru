#!/usr/bin/env python

import re
import urllib2

#response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82')

#html = response.read()
#print html

next_number = '12345'
#next_number = '3875'
for i in range(400):
    #next_number = [s for s in re.findall(r'\b\d+\b', html)][0]
    
    new_response = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + next_number
    response = urllib2.urlopen(new_response)
    html = response.read()
    
    try:

        next_number = re.search('and the next nothing is (\d+)', html).group(1)
        
    except:
        next_number = str(int(next_number)/2)
        print html  
