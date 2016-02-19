#!/usr/bin/env python

a = range(1, 21)

# function to return double of input
def double_input(x):
    return x * 2

# function filters even numbers
def is_even(x):
    return x % 2 == 0

# function to sum
def sum(x,y):
    return x +y


# old way:
c = []
for i in a:
    c.append(i*2)

# using map - map allows you to map a function to every item in a list. map returns a new list of
# items that are the items in the original list modified by the given func
b = map(double_input, a)

# using filter - we can filter a list to get items that return true to a given test function
d = filter(is_even, a)

# using reduce - continually applies given function to a given sequence. returns a signle value
e = reduce(sum, a)
# to error handle - can give initial value
g = []
f = reduce(sum, g, 10)

print 'C:'
print c

print 'B:'
print b

print 'D:'
print d

print 'E:'
print e

print 'F:'
print f


# the above is all nice and good . . .but LIST COMPREHENSION is where the real magic lies
print 'List Comprehension....'
# double:
print [x*2 for x in a]
# filter even:
print [x for x in a if x % 2 == 0]

