#! /bin/bash

def readfile(filename: str) -> list[list[str]]:
  crossWord = []
  with open(filename, 'r') as file:
    crossWord = [list(line.strip()) for line in file]

  return crossWord

def part2(crossWord: str) -> int:
  MAXROWS = len(crossWord)
  MAXCOLS = len(crossWord[0])

  def isShapeX(grid, row, col):
    if grid[row][col] != 'A':
      return False
    
    # upleft, downright
    diagonal1 = grid[row - 1][col - 1] + grid[row + 1][col + 1]
    # up right, downleft
    diagonal2 = grid[row + 1][col - 1] + grid[row - 1][col + 1]
  
    correct = set(['SM', 'MS'])
    return diagonal1 in correct and diagonal2 in correct
  
  count = 0
  for i in range(1, MAXROWS - 1):
    for j in range(1, MAXCOLS - 1):
        count += 1 if isShapeX(crossWord, i, j) else 0

  return count



filename = './input.txt'
# filename = './exampleInput.txt'
crossWord = readfile(filename)

for i in crossWord:
  print(i)

answer = part2(crossWord)
print(f'answer: {answer}')