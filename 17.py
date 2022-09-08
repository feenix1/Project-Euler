onesList = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teensList = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tensList = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",]
hundredsList = ["", "onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]
thousandsList = ["", "onethousand"]

writtenNumList = []

for num in range(0, 1001):
  reversedNumString = reversed(str(num))
  
  onesPlaceString = ""
  tensPlaceString = ""
  hundredsPlaceString = ""
  thousandsPlaceString = ""
  
  andInNum = False
  
  for digit, value in enumerate(reversedNumString):
    value = int(value)
    
    # ones place
    if digit == 0:
      onesPlaceString = onesList[value]
      onesPlace_MEM = value
    # tens place
    if digit == 1:
      tensPlace_MEM = value
      if value == 1:
        tensPlaceString = teensList[onesPlace_MEM]
        onesPlaceString = ""
      if value > 1 and onesPlace_MEM == 0:
        tensPlaceString = tensList[value]  
        onesPlaceString = ""
      if not value == 1 or (value > 1 and onesPlace_MEM == 0):
        tensPlaceString = tensList[value]
    # hundreds place + and bool
    if digit == 2:
      andInNum = True
      hundredsPlaceString = hundredsList[value]
      if onesPlace_MEM == 0:
        onesPlaceString = ""
        if tensPlace_MEM == 0:
          andInNum = False
    # thousands place
    if digit == 3:
      thousandsPlaceString = thousandsList[value]

  writtenNum = ""

  if andInNum:
    andString = "and"
  else:
    andString = ""
    
  writtenNum = thousandsPlaceString + hundredsPlaceString + andString + tensPlaceString + onesPlaceString
  writtenNumList.append(writtenNum)

for num in range(1, 1001):
  print(f"{num}: {writtenNumList[num]}", end = "\n")

totalLetters = 0

for writtenNum in writtenNumList:
  totalLetters += len(writtenNum)

print(f"Total letters: {totalLetters}")