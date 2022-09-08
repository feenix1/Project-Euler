number = 20

# Takes ages but does eventually give the right answer

while True:
  divisible = True
  for div in range(2, 21):
    if number % div == 0:
      continue
    else:
      divisible = False
      break
  if number % 1000000 == 0:
    print(f"Numbers Scanned: {number}",end="\r")
  
  if divisible == True:
    print("Smallest number divisible by 1-20: {}".format(number))
    break
  
  number += 20