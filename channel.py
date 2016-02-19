#!/usr/bin/env python

import re
import urllib2
import zipfile
import StringIO

zipy = zipfile.ZipFile(StringIO.StringIO(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read()))

file_num = '90052'
good_files = []
while True:
    #file_name = file_num + '.txt' 
    try:
        file_name = file_num + '.txt'
        contents = zipy.read(file_name)
        print contents
        file_num = re.search('Next nothing is (\d+)', contents).group(1)
        good_files.append(file_name)
        
    except:
        print "BREAKING"
        break

# answer lies in the comments of each file
print ''.join(zipy.getinfo(name).comment for name in good_files)
