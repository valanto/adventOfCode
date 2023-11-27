import os

def part2():
  pairs=0

  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    (elf1, elf2) = line.split(",")
    (elf1_start, elf1_end) = elf1.strip().split("-")
    (elf2_start, elf2_end) = elf2.strip().split("-")

    elf1_start = int(elf1_start)
    elf1_end = int(elf1_end)
    elf2_start = int(elf2_start)
    elf2_end = int(elf2_end)

    elf1_range = range(elf1_start, elf1_end+1)
    elf2_range = range(elf2_start, elf2_end+1)

    if len(set(elf1_range).intersection(elf2_range)) > 0:
      pairs +=1

  return pairs
  
def part1():
  pairs=0

  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    (elf1, elf2) = line.split(",")
    (elf1_start, elf1_end) = elf1.strip().split("-")
    (elf2_start, elf2_end) = elf2.strip().split("-")

    elf1_start = int(elf1_start)
    elf1_end = int(elf1_end)
    elf2_start = int(elf2_start)
    elf2_end = int(elf2_end)

    if (elf1_start >= elf2_start and elf1_end <=elf2_end) or (elf2_start >= elf1_start and elf2_end <= elf1_end):
      pairs +=1

  return pairs


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
