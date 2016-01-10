#!/usr/bin/python

"""Each new term in the Fibonnacci sequence is generated by adding the previus two terms. \
By starting with 1 and 2, the first 10 terms will be:\
1,2,3,5,8,13,21,34,55,89,...\
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def fibonacci(car,value,end):
  if value > end:
   return 1
  else:
    total = value
    total += fibonacci(value, car + value , end)
    return total

total = fibonacci(1,2,4000000)
print "The sum of the even-valued terms is", total
