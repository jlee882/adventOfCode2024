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
  def safe(report):
    if report[0] > report[1]:
      report.reverse()
    
    for i in range(1, len(report)):
      if report[i] - report[i - 1] not in range(1, 4):
        return False
    return True
  
  safeCount = 0
  for r in reports:
    for i in range(len(r)):
      r2 = r[0:i] + r[i+1:]
      if safe(r2):
        safeCount += 1
        break

  return safeCount


# fileName = './exampleInput.txt'
fileName = './input.txt'
reports = readInput(fileName)
print(reports[0])
answer = calcSafeReports(reports)
print(answer)


