#! /bin/usr/python3

import re

def calculate(input_string):
  matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)', input_string)
  answer = 0

  skip = False
  for i in matches:
    if i == 'don\'t()':
      skip = True
    elif i == 'do()':
      skip = False
    elif not skip:
      parsed = i.split(',')
      operand1, operand2 = parsed[0][4:], parsed[1][0:-1]
      answer += int(operand1) * int(operand2)

  return answer

filename = './input.txt'
# filename = './exampleInput2.txt'
input_string = open(filename, 'r').read()
answer = calculate(input_string)
print(answer)