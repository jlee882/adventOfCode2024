#! /bin/bash

def readfile(filename: str) -> list[list[str]]:
  crossWord = []
  with open(filename, 'r') as file:
    crossWord = [list(line.strip()) for line in file]

  return crossWord

def part1(crossWord: str) -> int:
  SEARCHWORD = 'XMAS'
  MAXROWS = len(crossWord)
  MAXCOLS = len(crossWord[0])
  
  # up, down, left, right, upleft, upright, downleft, downright
  xDirection = [0, 0, -1, 1, -1, 1, -1, 1]
  yDirection = [-1, 1, 0, 0, -1, -1, 1, 1]

  def isWordInDirection(grid, target, row, col, xdir, ydir):
    currX, currY = row, col
    for i in range(len(target)):
      # bounds check
      if currX < 0 or currY < 0 or currX >= MAXCOLS or currY >= MAXROWS:
        return 0
      elif grid[currX][currY] != target[i]:
        return 0
      
      currX += xdir
      currY += ydir

    return 1
  
  count = 0
  for i in range(MAXROWS):
    for j in range(MAXCOLS):
      if crossWord[i][j] == SEARCHWORD[0]:
        for k in range(8):
          count += isWordInDirection(crossWord, SEARCHWORD, i, j, xDirection[k], yDirection[k])

  return count



filename = './input.txt'
# filename = './exampleInput.txt'
crossWord = readfile(filename)

for i in crossWord:
  print(i)

answer = part1(crossWord)
print(f'answer: {answer}')


################## Notes ############################
# Don't try all the cases when you can generalize it like vector ...
  # def checkUp(target, row, col, grid):
  #   targetLen = len(target) - 1
  #   if row - targetLen + 1 >= 0 and all(target[i] == grid[row - i][col] for i in range(targetLen)):
  #     return 1
  #   return 0
  
  # def checkDown(target, row, col, grid):
  #   targetLen = len(target)
  #   if row + targetLen - 1 < MAXROWS and all(target[i] == grid[row + i][col] for i in range(targetLen)):
  #     return 1
  #   return 0
  
  # def checkLeft(target, row, col, grid):
  #   targetLen = len(target)
  #   if col - targetLen + 1 > 0 and all(target[j] == grid[row][col - j] for j in range(targetLen)):
  #     return 1
  #   return 0
  
  # def checkRight(target, row, col, grid):
  #   targetLen = len(target)
  #   if col + targetLen - 1 < MAXCOLS and all(target[j] == grid[row][col + j] for j in range(targetLen)):
  #     return 1
  #   return 0
  
  # def checkUpLeft(target, row, col, grid):
  #   targetLen = len(target)
  #   if row - targetLen + 1 >= 0 and col - targetLen + 1 > 0:
  #     if all(target[k] == grid[row - k][col - k] for k in range(targetLen)):
  #       return 1
  #   return 0
  
  # def checkUpRight(target, row, col, grid):
  #   targetLen = len(target)
  #   if row - targetLen + 1 >= 0 and col - targetLen + 1 > 0:
  #     if all(target[k] == grid[row - k][col - k] for k in range(targetLen)):
  #       return 1
  #   return 0