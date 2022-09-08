import math as m

sequenceLength = []

for startNum in range(1, 1000000):
  n = startNum
  sequence = []
  while n != 1:
    # print("startNum: {} | Num: {}".format(startNum, n), end = "\r")
    sequence.append(n)
    if n % 2 == 0:
      n = n / 2
    else:
      n = (3 * n) + 1
  
  sequenceLength.append(len(sequence) + 1)

  if ".000" in str((100 * startNum) / 1000000):
    print("Percent Complete: {}%".format(m.floor((100 * startNum) / 1000000)), end = "\r")

  
maxLength = 0
maxLengthIndex = 0

for index, length in enumerate(sequenceLength):
  if length > maxLength:
    maxLength = length
    maxLengthIndex = index

print("The number with the longest chain is: {}".format(maxLengthIndex + 1))
