#!/usr/bin/env python

# investigating __name__ and if __name__ == '__main__'

# this code here will always be run
print "Always run: First module's name: {}".format(__name__)

# before python interprets code, it sets some default variables: __name__ is one of them
# can import module: when doing so, it sets __name__ to the module file name

def main():
    print "This is run by the main module. First Module's Name: {}".format(__name__)

# allows us to run code only if this script is the main script - i.e. directly executed
# sometimes code that only runs if the main file or only run if imported
if __name__ == '__main__':
    main()
else:
    print "This file was imported"

"""
Preferred Syntax:

# code this will always be run

def main():
    function to contain code to only be run if main module

if __name__ == '__main__':
    main()

"""
