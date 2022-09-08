import math as m

sum = 0
percent = 0

for base in range(1, 1001):
    num = 0
    num = base ** base
    sum += num

counter = 0
string = ""

for digit in reversed(str(sum)):
    string += digit
    if counter == 9:
        break
    counter += 1

newString = ""

for digit in reversed(string):
    newString += digit

print(newString)
