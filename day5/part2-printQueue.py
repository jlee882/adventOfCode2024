#! /bin/usr/python3
from functools import cmp_to_key

def readInput(filename):
  rules = []
  updatePages = []
  with open(filename, 'r') as file:
    readRules = True
    for line in file:
      line = line.strip()
      if line == '':
        readRules = False
      elif readRules:
        rules.append(line.split('|'))
      else:
        updatePages.append(line.split(','))

  return (rules, updatePages)

def part2(rules: list[list[str]], updatePages: list[list[str]]) -> int:
  def checkRule(rule: list[str], pageSeqDict: dict):
    first = rule[0]
    last = rule[1]
    
    return pageSeqDict.get(first, -1) < pageSeqDict.get(last, len(pageSeqDict))

  rulesDict = {}
  for first, second in rules:
    if first not in rulesDict:
      rulesDict[first] = set()
    
    rulesDict[first].add(second)

  def compare(x: str, y: str):
    if x in rulesDict and y in rulesDict[x]:
      return -1
    elif y in rulesDict and x in rulesDict[y]:
      return 1
    return 0

  sumIncorrect = 0
  for seq in updatePages:
    seqDict = {value: index for index, value in enumerate(seq)}
    if not all(checkRule(r, seqDict) for r in rules):
      seq = sorted(seq, key=cmp_to_key(compare))
      print(seq)
      sumIncorrect += int(seq[len(seq) // 2])
      

  return sumIncorrect

filename = './input.txt'
# filename = './exampleInput.txt'

rules, pages = readInput(filename)

answer = part2(rules, pages)
print(f'answer: {answer}')

    
