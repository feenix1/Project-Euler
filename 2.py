a = 1
b = 0
c = 0

num = 0
evenTerms = []

while c <= 4000000:
  num += 1
  c = a + b
  a = b
  b = c
  print("Fib Seq Num: {} | Length: {}".format(num, len(evenTerms), end = "\r"))
  
  if (c % 2) == 0:
    evenTerms.append(c)

print("")
print("Sum of all even Fib term (to 4 mil) is: {}".format(sum(evenTerms)))