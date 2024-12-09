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

def part1(operands: list[list[int]]):
  sumTotal = 0
  # operators = ['*', '+']
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
      multResult = backTrack(numbers, index + 1, total * numbers[index])
      return max(addResult, multResult)
    
  for i in operands:
    sumTotal += backTrack(i, 1, 0)

  return sumTotal

filename = './input.txt'
# filename = './exampleInput.txt'
input = readInput(filename)

answer = part1(input)
print(f'answer: {answer}')

