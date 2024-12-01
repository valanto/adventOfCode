import os
import re

def part2():
  list_1 = []
  list_2 = []
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    if line.strip():
      joined = re.match(r"^(\d+)\s+(\d+)$", line.strip())
      list_1.append(int(joined[1]))
      list_2.append(int(joined[2]))
  
  total = 0
  
  for i in range(len(list_1)):
      num_in_question = list_1[i]
      appearances=0
      for x in list_2:  
        if x == num_in_question:
          appearances = appearances + 1
      total = total + num_in_question*appearances
  
  return total

def part1():
  list_1 = []
  list_2 = []
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    if line.strip():
      joined = re.match(r"^(\d+)\s+(\d+)$", line.strip())
      list_1.append(int(joined[1]))
      list_2.append(int(joined[2]))
  list_1.sort()
  list_2.sort()
  
  diffs = []
  
  for i in range(len(list_1)):
      diffs.append(abs(list_1[i]-list_2[i]))
  
  return sum(diffs)

print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
