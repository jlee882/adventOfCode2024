#! /bin/usr/python3

def readInput(filename: str) -> str:
  inputString = ''
  with open(filename, 'r') as file:
    line = file.readline()
    inputString = line.strip()

  return inputString
    

def part1(input: str) -> int:
  def transformToMemory(encoded: str) -> list:
    memory = []
    if len(encoded) % 2 == 1:
      encoded = encoded + '0' # add dummy free space

    for i in range(0, len(encoded), 2):
      id = i // 2
      blocksMem = int(encoded[i])
      blocksFree = int(encoded[i + 1])

      memory += [id] * blocksMem
      memory += ['.'] * blocksFree
    
    return memory
  
  def compact(memory: list) -> list:
    right = len(memory) - 1
    try:
      left = memory.index('.')
      while right > left:
        if memory[right] != '.':
          memory[left], memory[right] = memory[right], memory[left]
          right -= 1
          left = memory.index('.', left + 1)
        else:
          right -= 1

      return memory[:left]
    except:
      print('No free memory')
      return memory

  memory = transformToMemory(input)
  memory = compact(memory)

  return sum([i * val for i, val in enumerate(memory)])

# filename = './exampleInput.txt'
filename = './input.txt'
input = readInput(filename)
answer = part1(input)

print(f'answer: {answer}')