# Starting in the top left corner of a 2×2 grid, and only being able to move to the 
# right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# ================================================================================

# each point in the grid has a set amount of routes to get to the end
# starting from the end, we can work our way back to the beginning to find
# how many routes are possible, by adding the possible routes of the points
# right and down from the beginning.

# because there are 21 points on the 20 wide grid
gridLength = 21

gridList = []

# create the gridList with rows and points
for row in range(0, gridLength):
  rowList = []
  for point in range(0, gridLength):
    rowList.append(0)
  gridList.append(rowList)

# to simplify, we'll start in the top left corner as if it were the end point
# and calculate the points in each row

for rowIndex, row in enumerate(gridList):
  for pointIndex, point in enumerate(row):
    # end point has no routes; you're already there
    if rowIndex == 0 and pointIndex == 0:
      gridList[rowIndex][pointIndex] = 0
    # in a line, there is only one route
    elif rowIndex == 0 or pointIndex == 0:
      gridList[rowIndex][pointIndex] = 1
    # else, take the sum of the points to the left and top
    else:
      gridList[rowIndex][pointIndex] = gridList[rowIndex - 1][pointIndex] + gridList[rowIndex][pointIndex - 1]

# print the gridList
for row in gridList:
  print(row, end="\n")

print("")
  
# print the value at the "end" (the beginning) for the answer
print(gridList[gridLength - 1][gridLength - 1])