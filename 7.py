# Project Euler 7

# What is the 10,001st prime number?

primeDivList = [2]
primeList = []

# Starts at 2 since 0 and 1 aren't technically prime
num = 2
while len(primeList) < 10001:
  prime = False
  for prime in primeDivList:
    # If num being checked is in the list of prime numbers 
    if prime >= num:
      prime = True
      break
    if (num % prime) == 0:
      break
    else:
      prime = True
  
  if prime == True:
    primeList.append(num)
    if num > primeDivList[len(primeDivList) - 1]:
      primeDivList.append(num)

  if len(primeList) % 100 == 0:
    print(f"Length of primeList: {len(primeList)}",end="\r")
    
  num += 1

print("")
print(primeList[len(primeList) - 1])