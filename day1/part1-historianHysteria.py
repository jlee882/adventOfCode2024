#! /bin/usr/python3

def calcTotalDistance(array1, array2):
  array1.sort()
  array2.sort()
  distance = 0
  for i in range(0,len(array1)):
    distance += abs(array1[i] - array2[i])

  return distance

def readInput(filename):
  array1 = []
  array2 = []
  with open(filename, 'r') as file:
    for line in file:
      line = line.strip()
      fields = line.split()
      array1.append(int(fields[0]))
      array2.append(int(fields[1]))

  return (array1, array2)


fileName = './input.txt'
#fileName = './day1-exampleInput.txt'
array1, array2 = readInput(fileName)

print(array1[0], array2[0])
answer = calcTotalDistance(array1, array2)
print(f'distance: {answer}')