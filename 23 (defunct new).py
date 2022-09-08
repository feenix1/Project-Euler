from multiprocessing.connection import wait
from multiprocessing.sharedctypes import Value
import os
import random
import math as m
import datetime as dt
from re import L
from time import sleep

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors 
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as 
# the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. A perfect number is a number for which the 
# sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this 
# upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two 
# abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def perf(func, *args):
    start = dt.datetime.now()
    output = func(*args)
    return output, dt.datetime.now() - start

def is_int(n):
    if n == int(n):
        return True
    else:
        return False

def find_divisors(n):
    dlist = [1]
    for dvnd in range(2, m.floor(m.sqrt(n))):
        dvsr = n / dvnd
        if is_int(dvsr):
            dlist.append(int(dvnd))
            dlist.append(int(dvsr))
    dlist.sort()
    return dlist

def is_abundant(n):
    if sum(find_divisors(n)) > n:
        return True
    return False

def find_abundant(n):
    alist = []
    for i in range(1, n):
        if is_abundant(i):
            alist.append(i)
    return alist

    