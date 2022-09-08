import os
import datetime

def clear():
  os.system('clear' if os.name == 'posix' else 'cls')

def int_input(message, range1 = "null", range2 = "null"):
  while True:
    try:
      output = int(input(str(message)))

      if range1 != "null":
        if output < int(range1):
          print("Invalid value, please try again.\n")
          continue
         
      if range2 != "null":
        if output > range2:
          print("Invalid value, please try again.\n")
          continue
      return output
      break
    except ValueError:
      print("Invalid value, please try again.\n")
      continue


def bool_input(message, trueString = "y", falseString = "n"):
  while True:
    output = input(str(message))

    if output == trueString:
      return True
      break
    if output == falseString:
      return False
      break
    else:
      print("Invalid value, please try again.")
      continue
# =====================================================================
validList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 25, 29, 30, 34, 36, 39, 48]

while True:
  print("Numbers are indexed by their order on the Project Euler page.")
  print("")
  print("Valid inputs: {}".format(validList))
  print("Extension Count: {}".format(len(validList)))
  print("")
  run = int_input("Input the extension number to run here: ", 0)

  runString = str(run) + ".py"

  print("")
  timeStart = datetime.datetime.now()
  exec(open(runString).read())
  timeEnd = datetime.datetime.now() 
  print("-----------------------------------------------------")
  print("Execution Time was " + str(timeEnd - timeStart))
  print("")
  input("Press enter to continue.")
  clear()