# Consider all integer combinations of  for 2 ≤  ≤ 5 and 2 ≤  ≤ 5:

# If they are then placed in numerical order, with any repeats 
# removed, we get the following sequence of 15 distinct terms:

# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

# How many distinct terms are in the sequence generated 
# by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

base = 2
power = 2

term = 0

termsList = []

while base <= 100:
  power = 2
  while power <= 100:
    term = 0
    term = base ** power

    if term not in termsList:
      termsList.append(term)
    power += 1
    
  base += 1

print("Length: " + str(len(termsList)))