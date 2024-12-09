#! /bin/usr/python3

import math

def readInput(filename: str) -> list:
  city = []
  with open(filename, 'r') as file:
    for line in file:
      line = line.strip()
      city.append(list(line))

  return city

def part2(city: list) -> int:
  uniqueCount = 0
  antennaLoc = {}
  for i in range(len(city)):
    for j in range(len(city[i])):
      antenna = city[i][j]
      if antenna != '.':
        if antenna in antennaLoc:
          antennaLoc[antenna].append((i, j))
        else:
          antennaLoc[antenna] = [(i, j)]

  for antennaFreq, antennaPositions in antennaLoc.items():
    for i in range(len(antennaPositions)):
      antenna1 = antennaPositions[i]
      for j in range(i + 1, len(antennaPositions)):
        antenna2 = antennaPositions[j]
        deltaY = antenna1[0] - antenna2[0]
        deltaX = antenna1[1] - antenna2[1]

        gcd = math.gcd(deltaX, deltaY)
        deltaY = deltaY // gcd
        deltaX = deltaX //gcd

        row, col = antenna2[0], antenna2[1]

        while row >= 0 and row < len(city) and col >= 0 and col < len(city[0]):
          if city[row][col] != '#':
            city[row][col] = '#'
            uniqueCount += 1
          row += deltaY
          col += deltaX

        row, col = antenna2[0] - deltaY, antenna2[1] - deltaX
        while row >= 0 and row < len(city) and col >= 0 and col < len(city[0]):
          if city[row][col] != '#':
            city[row][col] = '#'
            uniqueCount += 1
          row -= deltaY
          col -= deltaX

  return uniqueCount

filename = './input.txt'
# filename = './exampleInput.txt'

city = readInput(filename)
answer = part2(city)
print(f'answer: {answer}')


