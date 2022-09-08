import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

power5num = []
numString = ""

# Upper range is 295245 because thats what other people
# found to be the upper bound solving the equation 
# upperBound = digits * (9 ** 5).

# I don't really get it right now, but it's definitely
# something that could be explained later.

for num in range(10, 295245):
  numString = str(num)  
  sumDigits = 0
  for digit in numString:
    sumDigits += int(digit) ** 5
  if num == sumDigits:
    power5num.append(num)

  # print("Num: {} | Length: {}".format(num, len(power5num)), end = "\r")

clear()

print("Numbers that fit criteria are:")
print(power5num)
print("")
print("Sum of all these numbers is: {}".format(sum(power5num)))