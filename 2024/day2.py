import os
import re

def generate_list():
  l = []
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    if line.strip():
      joined = re.findall(r"(\d+)\s*", line.strip())
      record = []
      for j in joined:
        record.append(int(j))
      l.append(record)

  return l


def check_report(report):
  previous = None
  direction = None
  checked = 0
  for entry in report:
    if previous is not None:
      diff = previous - entry
      if direction is None:
        direction = 1 if diff < 0 else 0
      
      if abs(diff) < 1 or abs(diff) > 3 or(diff > 0 and direction == 1) or (diff < 0 and direction == 0):
        break 
    previous = entry
    checked +=1
  if checked == len(report):
    return True
  return False


def part2():
  reports = generate_list()
  safe = 0
  for report in reports:
    if check_report(report):
      safe+=1
    else:
      for idx,entry in enumerate(report):
        new_report = report.copy()
        new_report.pop(idx)
        if check_report(new_report):
          safe+=1
          break
  return safe

def part1():
  reports = generate_list()
  safe = 0
  for report in reports:
    if check_report(report):
      safe +=1
      
  
  return safe

print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
