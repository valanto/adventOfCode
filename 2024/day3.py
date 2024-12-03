import os
import re

def generate_list():
  l = []
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  should_multiply=True
  for line in file:
    if line.strip():
      matches = re.findall(r"(don't\(\))|(do\(\))|(mul\(\d{1,3},\d{1,3}\))", line.strip())
      for idx, match in enumerate(matches):
        (dont, do, mul) = match
        if dont:
          should_multiply= False
        elif do:
          should_multiply=True
        elif mul:
          multiply = re.match(r"^mul\((\d{1,3}),(\d{1,3})\)$", mul)
          (left, right)=multiply.groups()
          l.append(([int(left), int(right)],should_multiply))

  return l


def part2():
  multiplications = generate_list()
  sum = 0
  for pair, should_multiply in multiplications:
    if should_multiply:
      sum += pair[0]*pair[1]
  
  return sum

def part1():
  multiplications = generate_list()
  sum = 0
  for pair, should_multiply in multiplications:
    sum += pair[0]*pair[1]
  
  return sum

print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
