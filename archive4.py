#!/usr/bin/python

""" A palindromic number reads the same both ways. The larguest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. """
""" Find the larguest palindrome made from the product of two 3-digit numbers. """

def is_palindrome(number):
  word = list(str(number))
  return word == word[::-1]

def generator(digits):
  values = [(x*y,x,y) for x in range(1,10**digits) for y in range(1,10**digits) if is_palindrome(x*y) ]
  return values

values = generator(3)
result = max(values, key= lambda item:item[0])

print "The max value %s is the result of %s * %s" % result
