#! /bin/usr/python3

def readInput(filename: str):
  operands = []
  with open(filename, 'r') as file:
    for line in file:
      line = line.strip()
      line = line.replace(':', '' )
      lineList = line.split()
      lineList = [int(x) for x in lineList]
      operands.append(lineList)

  return operands

def part2(operands: list[list[int]]):
  sumTotal = 0
  def backTrack(numbers: list[int], index: int, total: int):
    target = numbers[0]
    if total > target:
      return 0
    elif index == len(numbers):
      if total == target:
        return target
      return 0
    else:
      addResult = backTrack(numbers, index + 1, total + numbers[index])
      if addResult != 0:
        return addResult
      multResult = backTrack(numbers, index + 1, total * numbers[index])
      if multResult != 0:
        return multResult
      concatTotalInput = str(total) + str(numbers[index])
      concatResult = backTrack(numbers, index + 1, int(concatTotalInput))
      return concatResult
    
  for i in operands:
    sumTotal += backTrack(i, 1, 0)

  return sumTotal

filename = './input.txt'
# filename = './exampleInput.txt'
input = readInput(filename)

answer = part2(input)
print(f'answer: {answer}')

