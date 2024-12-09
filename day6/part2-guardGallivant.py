#! /bin/usr/python3
import copy
def readInput(filename: str) -> list[list[str]]:
  labMap = []
  with open(filename, 'r') as file:
    for line in file:
      line = line.strip()
      labMap.append(list(line))

  return labMap

def part2(labMap: list):
  # find guard
  def findGuard(labMap: list):
    guard = '^'
    for i in range(len(labMap)):
      for j in range(len(labMap[i])):
        if labMap[i][j] == guard:
          return (i, j)
    raise Exception('No guard found')
  
  guardStart = findGuard(labMap)
  # 0 - up, 1 - right, 2 - down, 3 - left
  directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] 
  labMapOriginal = copy.deepcopy(labMap)

  countTrap = 0
  for x in range(len(labMap)):
    print(f'finish row {x}')
    for y in range(len(labMap[x])):
      if '^' != labMap[x][y] != '#':
        labMap = copy.deepcopy(labMapOriginal)
        currDir = 0
        visited = {
          0: set(), # up
          1: set(), # right
          2: set(), # down
          3: set() # left
        }
        i, j = guardStart
        prev = guardStart
        labMap[i][j] = '.'
        labMap[x][y] = '#'

        while i >= 0 and j >= 0 and i < len(labMap) and j < len(labMap[i]):
          if labMap[i][j] == '.':
            labMap[i][j] = 'x'
          elif labMap[i][j] == '#':
            i, j = prev
            currDir = (currDir + 1) % 4
          elif labMap[i][j] == 'x' and f'{i},{j}' in visited[currDir]:
            # for i in labMap:
            #   print(i)
            # print(visited)
            # print('-------------------------')
            countTrap += 1
            break

          visited[currDir].add(f'{i},{j}')
          prev = (i, j)
          i += directions[currDir][0]
          j += directions[currDir][1]

  return countTrap

filename = './input.txt'
# filename = './exampleInput.txt'
labMap = readInput(filename)
answer = part2(labMap)
print(f'answer: {answer}')


