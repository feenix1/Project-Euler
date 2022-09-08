def int_input(message, range1 = "null", range2 = "null"):
  while True:
    try:
      output = int(input(str(message)))

      if range1 != "null":
        if output < int(range1):
          print("Invalid value, please try again.\n")
          continue
         
      if range2 != "null":
        if output > range2:
          print("Invalid value, please try again.\n")
          continue
      return output
      break
    except ValueError:
      print("Invalid value, please try again.\n")
      continue

# ==========================================================================================

import math as m

approach = int_input("Which approach? [0] [1]: ", 0, 1)

# ==========================================================================================

if approach == 0:
  primeDivList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
  primeList = []
  
  # Starts at 2 since 0 and 1 aren't technically prime
  for num in range(2, 2000000):
    prime = False
    for prime in primeDivList:
      # If num being checked is in the list of prime numbers 
      if prime >= num ** 0.5:
        prime = True
        break
      if (num % prime) == 0:
        break
      else:
        prime = True
    
    if prime == True:
      primeList.append(num)
      if num > 997:
        primeDivList.append(num)
    else:
      continue
  
    sumOf = sum(primeList)
    length = len(primeList)

    if ".000" in str((100 * num) / 2000000):
      print("Percent Complete: {}%".format(m.floor((100 * num) / 2000000)), end = "\r")
  
  print("Sum is {}".format(sumOf))

# ===================================================================================

if approach == 1:
  # -----------------------------------------------------------------------------------
  # Theres an interesting little algorithim to quickly find all the primes to a certain
  # value called the Sieve of Eratosthenes. Found it on Stack Overflow, and I'll do my
  # best to implement it here.
  #
  # It's known to be pretty memory intesive, although light on proccessing.
  #
  # This should be faster than the previous "divide every number by all the other prime
  # numbers" approach. However, since that currently doesn't provide the right answer, 
  # the other will be the fallback approach.
  # -----------------------------------------------------------------------------------

  numList = []
  for _ in range(0, 2000000):
    if _ == 0 or _ == 1:
      numList.append(False)
    else:
      numList.append(True)

  # Created with extensive help from https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  # Not sure how the optimzation of only checking i's lower than 2000000's sqrt works,
  # but that's something that can be explained later.
      
  for i in range(2, m.floor(2000000 ** 0.5)):
    if numList[i] == True:
      j = i ** 2
      multiplyi = 1
      while j < 2000000:
        numList[j] = False
        multiplyi += 1
        j = (i ** 2) + (i * multiplyi)
        if i == 5:
          print("i: {}".format(i), end = "\r")
      
  # print(numList)
  
  primeList = []
  
  for index, num in enumerate(numList):
    if num == True:
      primeList.append(index + 2)

  print(primeList)

  print("All primes below 2 mil are: {}".format(primeList))