import os
import datetime

def clear():
  os.system('clear' if os.name == 'posix' else 'cls')

def bold(message):
  return "\033[1m" + message + "\033[0m"

def int_input(message, range1 = "nil", range2 = "nil", bpsMessage = "nil"):
  while True:
    try:
      output_raw = input(str(message))
      
      if bpsMessage != "nil":
        if output_raw == bpsMessage:
          return bpsMessage

      output = int(output_raw)

      if range1 != "nil":
        if output < int(range1):
          print("Invalid value, please try again.\n")
          continue
         
      if range2 != "nil":
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
defunctList = [23, 24]

clear()

while True:
  print("Numbers are indexed by their order on the Project Euler page.")
  print("Type 'exit' to exit the program.")
  print("")
  print("{} Valid inputs: {}".format(len(validList), validList))
  print("{} Defunct inputs: {}".format(len(defunctList), defunctList))
  print("Total Extension Count: {}".format(len(validList) + len(defunctList)))
  print("")
  
  run = int_input("Input the extension number to run here: ", 0, "nil", "exit")
  if run == "exit":
    break
  
  if run in defunctList:
    print("This problem is defunct/work in progress, please choose another.")
    print("-----------------------------------------------------")
  elif run in validList:
    runString = str(run) + ".py"

    print("")
    timeStart = datetime.datetime.now()
    exec(open(runString).read())
    timeEnd = datetime.datetime.now()

    print("-----------------------------------------------------")
    print("Execution Time was " + str(timeEnd - timeStart))
  else:
    print("Invalid input, please try again.")
    print("-----------------------------------------------------")

  print("")
  input("Press enter to continue.")
  clear()