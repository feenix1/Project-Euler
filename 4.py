import math as m
import os

def clear():
  os.system('clear' if os.name == 'posix' else 'cls')

def isPalindrome(n):
  n = str(n)
  nHalfLength = m.floor(len(n) / 2)
  nhalf = ""
  nhalf2 = ""
  for index, char in enumerate(n):
    if index != nHalfLength:
      nhalf += char
    else:
      break

  for index, char in enumerate(reversed(n)):
    if index != nHalfLength:
      nhalf2 += (char)
    else:
      break

  if nhalf == nhalf2:
    return True
  else:
    return False

products = []

for factor1 in range(100, 1000):
  for factor2 in range(100, 1000):
    if factor1 > factor2:
      continue
    else:
      products.append(factor1 * factor2)


maxPdromeIndex = 0
maxPdrome = 0

for index, product in enumerate(products):
  if isPalindrome(product) == True:
    if product > maxPdrome:
      maxPdrome = product
      maxPdromeIndex = index
    else:
      continue

clear()

print("Highest Palindrome Value is: {}".format(maxPdrome))
