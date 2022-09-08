# A perfect number is a number for which the sum of its proper divisors is exactly 
# equal to the number. For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
# number that can be written as the sum of two abundant numbers is 24. 

# By mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. However, this upper limit 
# cannot be reduced any further by analysis even though it is known that the 
# greatest number that cannot be expressed as the sum of two abundant numbers is 
# less than this limit.

# Find the sum of all the positive integers that cannot be written as the sum of 
# two abundant numbers.

import math as m
import datetime

def sumOfDivisors(n):
  divList = []
  for div in range(1, m.floor(n ** 0.5)):
    if n % div == 0:
      divList.append(div)
      if not div == 1:
        divList.append(n // div)
  divList.sort()
  return sum(divList)

def isAbdnt(n):
  if sumOfDivisors(n) > n:
    return True
  return False

# ===========================================================

timeStart = datetime.datetime.now()
  
# Step 1: Find all abundant numbers less than 28123 - 12

abdntList = []

for num in range(12, 28123 - 12):
  if isAbdnt(num):
    abdntList.append(num)

print(len(abdntList), end="\n\n")
print(f"Excecution Time for Step 1: {datetime.datetime.now() - timeStart}", end="\n\n")

timeStart = datetime.datetime.now()

# Step 2: Find if the numbers between 1 and 28123 are able to be expressed as a sum of any
#         numbers in the abundant list

nonSumList = []
print(f"Excecution Time for Step 2: {datetime.datetime.now() - timeStart}", end="\n\n")

print(sum(nonSumList))
print(len(nonSumList))