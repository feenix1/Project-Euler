# What is the index of the first term in the Fibonacci sequence to contain 
# 1000 digits?

a = 1
b = 0
c = 0

index = 0

while len(str(c)) != 1000:
  c = a + b
  a = b
  b = c
  index += 1
  
print(c)
print("")
print(f"Index is: {index}")