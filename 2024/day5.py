import os
import re
import math

def generate_lists():
  rules = []
  updates = []
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    if line.strip():
      rule_match = re.match(r"^(\d+)\|(\d+)$", line.strip())
      if rule_match:
        rules.append((int(rule_match[1]), int(rule_match[2]),))
      else:
        updates_match = re.findall(r"(\d+)", line.strip())
        update = []
        for m in updates_match:
          update.append(int(m))
        updates.append(update)

  rule_d = dict()
  for (num1, num2) in rules:
    if num1 not in rule_d:
      rule_d[num1] = []
    rule_d[num1].append(num2)



    # if num1 not in rule_order and num2 not in rule_order:
    #   rule_order.append(num1)
    #   rule_order.append(num2)
    # elif num1 not in rule_order and num2 in rule_order:
    #   rule_order.insert(rule_order.index(num2), num1)
    # elif num1 in rule_order and num2 not in rule_order:
    #   rule_order.insert(rule_order.index(num1)+1, num2)
    # elif num1 in rule_order and num2 in rule_order and rule_order.index(num1)>rule_order.index(num2):
    #   rule_order.insert(rule_order.index(num1), rule_order.pop(rule_order.index(num2)))


  return (rule_d, updates)

def check(order, previous, current):
  return not(current in order and previous in order[current])

def part2():
  valid=0
  valid_middle_numbers = 0
  (rule_d,updates) = generate_lists()
  for update in updates:
    og=update.copy()
    previous=update[0]
    for c in range(len(update)):
      if c == 0:
        continue
      previous =update[c-1]
      current = update[c]
      while not check(rule_d, previous,current):
        fail=True
        update.insert(update.index(previous), update.pop(update.index(current)))
        if update.index(current) == 0:
          break
        previous = update[update.index(current)-1]
      c = c + 1
    if not all(x == y for x, y in zip(og, update)):
      valid_middle_numbers = valid_middle_numbers + update[math.ceil(len(og) / 2)-1]

  return valid_middle_numbers


def part1():
  valid=0
  valid_middle_numbers = 0
  (rule_d,updates) = generate_lists()
  for update in updates:
    og = update.copy()
    previous=update.pop(0)
    fail = False
    for current in update:
      if not check(rule_d, previous,current):
        fail = True
        break
      previous=current
    if not fail:
      valid_middle_numbers = valid_middle_numbers + og[math.ceil(len(og) / 2)-1]

  return valid_middle_numbers

print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
