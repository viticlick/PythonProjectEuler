#!/usr/bin/python

""" The prime factors of 13195 are 5,7,13 and 29 """
""" What is the larguest prime factor of the number 600851475143? """

def max_factor(n):
  divisor = 2
  while n > divisor:
    if n % divisor == 0:
      n = n / divisor
    else:
      divisor += 1
  return divisor

value1 = 13195
print "Larguest prime of %s is %s" % (str(value1) , str(max_factor(value1)))

value2 = 600851475143
print "Larguest prime of %s is %s" % (str(value2), str(max_factor(value2)))

