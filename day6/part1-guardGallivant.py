#! /bin/usr/python3

def readInput(filename: str) -> list[list[str]]:
  labMap = []
  with open(filename, 'r') as file:
    for line in file:
      line = line.strip()
      labMap.append(list(line))

  return labMap

def part1(labMap: list):
  # find guard
  def findGuard(labMap: list):
    guard = '^'
    for i in range(len(labMap)):
      for j in range(len(labMap[i])):
        if labMap[i][j] == guard:
          return (i, j)
    raise Exception('No guard found')
  
  i, j = findGuard(labMap)
  # 0 - up, 1 - right, 2 - down, 3 - left
  directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] 
  currDir = 0
  prev = None
  visited = 1
  labMap[i][j] = 'x'

  while i >= 0 and j >= 0 and i < len(labMap) and j < len(labMap[i]):
    if labMap[i][j] == '.':
      visited += 1
      labMap[i][j] = 'x'
    elif labMap[i][j] == '#':
      i, j = prev
      currDir = (currDir + 1) % 4

    prev = (i, j)
    i += directions[currDir][0]
    j += directions[currDir][1]

  return visited

filename = './input.txt'
# filename = './exampleInput.txt'
labMap = readInput(filename)
answer = part1(labMap)
print(f'answer: {answer}')


