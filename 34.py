# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import math as m

percent_mem = 0
percent = 0

factorialNumbers = []

for num in range(3, 9999999):
  digitFactorialSum = 0
  for digit in str(num):
    digitFactorialSum += m.factorial(int(digit))
  if digitFactorialSum == num:
    factorialNumbers.append(num)

  percent_mem = percent
  percent = m.floor((100 * num) / 9999999)
   
  if percent_mem != percent:
    print("Percent Complete: {}%".format(percent), end = "\r")

print("                                                     ")
print(factorialNumbers)
print("")
print(sum(factorialNumbers))