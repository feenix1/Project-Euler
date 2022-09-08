multipleList = []

for num in range (0, 1000):
  if num % 3 == 0:
    multipleList.append(num)
    continue
  elif num % 5 == 0:
    multipleList.append(num)
    continue

print(multipleList)
print("")
print("The sum of which is: ")
print(sum(multipleList))
