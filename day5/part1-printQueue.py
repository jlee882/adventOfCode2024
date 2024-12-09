#! /bin/usr/python3

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

def part1(rules: list[list[str]], updatePages: list[list[str]]) -> int:
  def checkRule(rule, pageSeqDict):
    first = rule[0]
    last = rule[1]
    
    return pageSeqDict.get(first, -1) < pageSeqDict.get(last, len(pageSeqDict))

  sumCorrect = 0
  for seq in updatePages:
    seqDict = {value: index for index, value in enumerate(seq)}
    if all(checkRule(r, seqDict) for r in rules):
      sumCorrect += int(seq[len(seq) // 2])

  return sumCorrect

filename = './input.txt'
# filename = './exampleInput.txt'

rules, pages = readInput(filename)

answer = part1(rules, pages)
print(f'answer: {answer}')

    
