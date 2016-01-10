#!/usr/bin/python

"""If we list all the natural numbers below 10 that are multiples of 3 or 5 \
we get 3, 5, 6 and 9. The sumof these multiples is 23.\
\
Find the sum of all the multiples of 3 or 5 below 1000."""

values = [ x for x in range(1,1001) if x % 3 == 0 or x % 5 == 0]
total = sum(values)

print "The result is", total

