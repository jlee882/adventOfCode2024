#! /bin/usr/python3

import re

def calculate(input_string):
  operands = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_string)
  answer = sum([int(x) * int(y) for x, y in operands])
  return answer

filename = './input.txt'
# filename = './exampleInput.txt'
input_string = open(filename, 'r').read()
answer = calculate(input_string)
print(answer)