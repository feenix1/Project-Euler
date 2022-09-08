sumOfSquares = 0
sumSquare = 0

for base in range(0, 101):
  sumOfSquares += base ** 2 
  sumSquare += base 

sumSquare = sumSquare ** 2

answer = sumSquare - sumOfSquares 

print(str(answer))