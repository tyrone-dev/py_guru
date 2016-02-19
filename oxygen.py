#!/usr/bin/env python

import Image

im = Image.open('oxygen.png')

width, height = im.size

print "".join([chr(im.getpixel((i, height/2))[0]) for i in range(0,width,7)])

print "".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
