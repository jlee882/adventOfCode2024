#! /bin/usr/python3

def readInput(fileName):
  reports = []
  with open(fileName, 'r') as file:
    for line in file:
      line = line.strip()
      report = line.split()
      report = [int(x) for x in report]
      reports.append(report)

  return reports

def calcSafeReports(reports):
  def unSafe(level1, level2):
    diff = level1 - level2
    return diff > 3 or diff < 1
  
  safeCount = len(reports)
  for r in reports:
    increaseFlag = r[0] < r[1]
    for i in range(1, len(r)):
      if (increaseFlag and unSafe(r[i], r[i-1])) or (not increaseFlag and unSafe(r[i-1], r[i])):
        safeCount -= 1
        break

  return safeCount

def calcSafeReports2(reports):
  def safe(report):
    if report[0] > report[1]:
      report.reverse()
    
    for i in range(1, len(report)):
      if report[i] - report[i - 1] not in range(1, 4):
        return False
    return True
  
  safeCount = 0
  for r in reports:
    safeCount += 1 if safe(r) else 0

  return safeCount


# fileName = './exampleInput.txt'
fileName = './input.txt'
reports = readInput(fileName)
print(reports[0])
answer = calcSafeReports(reports)
print(answer)
answer = calcSafeReports2(reports)
print(answer)


