import os


def part2():

  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    index = 0
    last14 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    for c in line.strip():
      last14 = last14[1:] + [c]
      if index >= 13 and len(set(last14)) == 14:
        return index+1
      index += 1

def part1():

  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    index = 0
    last4 = [None, None, None, None]
    for c in line.strip():
      last4 = last4[1:] + [c]
      if index >= 3 and len(set(last4)) == 4:
        return index+1
      index += 1


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
