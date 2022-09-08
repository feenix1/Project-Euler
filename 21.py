# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math as m

def sumOfDivisors(n):
  divList = []
  for div in range(1, m.floor(n ** 0.5)):
    if n % div == 0:
      divList.append(div)
      if not div == 1:
        divList.append(n // div)
  divList.sort()
  return sum(divList)

def isAmicable(n):
  if sumOfDivisors(sumOfDivisors(n)) == n and sumOfDivisors(n) != n:
    return True
  return False
  
amicList = []
lineWidth = 5
printed = 0

for testNum in range(1, 10000):
  if isAmicable(testNum):
    amicList.append(testNum)

    if printed % lineWidth == 0:
      print("\n")
    print(str(testNum) + ", ", end="")
    printed += 1

print("\n")
print(f"Sum of amicable numbers is: {sum(amicList)}")
