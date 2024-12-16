#! /bin/usr/python3

def readInput(filename: str) -> str:
  inputString = ''
  with open(filename, 'r') as file:
    line = file.readline()
    inputString = line.strip()

  return inputString
    

def part2(input: str) -> int:
  def transformToMemory(encoded: str) -> list:
    memory = []
    fileMap = {} # fileIndex : length
    freeMap = {} # startIndex: length

    if len(encoded) % 2 == 1:
      encoded = encoded + '0' # add dummy free space

    for i in range(0, len(encoded), 2):
      id = i // 2
      blocksMem = int(encoded[i])
      blocksFree = int(encoded[i + 1])

      memory += [id] * blocksMem
      fileMap[len(memory) - blocksMem] = blocksMem
      memory += ['.'] * blocksFree
      freeMap[len(memory) - blocksFree] = blocksFree
    
    return (memory, fileMap, freeMap)
  
  def compact(memory: list, fileMap: dict, freeMap: dict) -> list:
      fileIndexKeys = list(fileMap.keys())
      fileIndexKeys.sort()

      freeIndexKeys = list(freeMap.keys())
      freeIndexKeys.sort()

      fileKeyI = len(fileIndexKeys) - 1

      while fileKeyI >= 0:
        fileMemI = fileIndexKeys[fileKeyI]

        for index, freeMemI in enumerate(freeIndexKeys):
          if fileMemI <= freeMemI:
            break
          if fileMap[fileMemI] <= freeMap[freeMemI]:
            for i in range(fileMap[fileMemI]):
              memory[fileMemI + i], memory[freeMemI + i] = memory[freeMemI + i], memory[fileMemI + i]

            if fileMap[fileMemI] != freeMap[freeMemI]:
              newIndex = freeMemI + fileMap[fileMemI]
              remaining = freeMap[freeMemI] - fileMap[fileMemI]
              freeMap[newIndex] = remaining
              freeIndexKeys[index] = newIndex
            else:
              freeIndexKeys.pop(index)
            freeMap.pop(freeMemI, None)
            break

        fileKeyI -= 1 

      return memory

  memory, fileMap, freeMap = transformToMemory(input)
  memory = compact(memory, fileMap, freeMap)

  # print(''.join([str(i) for i in memory]))

  total = 0
  for i, v in enumerate(memory):
    if v != '.':
      total += i * v

  return total

# filename = './exampleInput.txt'
filename = './input.txt'
input = readInput(filename)
answer = part2(input)

print(f'answer: {answer}')

# 0099.111777244.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..
# 0099.111777.44.3332...5555.6666.....8888..