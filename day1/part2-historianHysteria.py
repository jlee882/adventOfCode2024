#! /bin/usr/python3

from collections import Counter

def calcSimilarityScore(array1, array2):
  similarity = 0
  counter = Counter(array2)
  for i in array1:
    similarity += i * counter[i]

  return similarity

def readInput(filename):
  array1 = []
  array2 = []
  # Open the file in read mode
  with open(filename, 'r') as file:
    for line in file:
      line = line.strip()
      fields = line.split()
      array1.append(int(fields[0]))
      array2.append(int(fields[1]))

  return (array1, array2)


fileName = './input.txt'
#fileName = './exampleInput.txt'
array1, array2 = readInput(fileName)

print(array1[0], array2[0])
answer = calcSimilarityScore(array1, array2)
print(f'Similarity Score: {answer}')