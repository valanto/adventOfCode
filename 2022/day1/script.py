import os


def part2():
  elves_calories = []
  current_calorie_count = 0

  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    if not line.strip():
      elves_calories.append(current_calorie_count)
      current_calorie_count = 0
    else:
      current_calorie_count += int(line)

  elves_calories.sort(reverse=True)
  return elves_calories[0] + elves_calories[1] + elves_calories[2]


def part1():
  highest_calorie_count = 0
  current_calorie_count = 0

  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    if not line.strip():
      if current_calorie_count > highest_calorie_count:
        highest_calorie_count = current_calorie_count
      current_calorie_count = 0
    else:
      current_calorie_count += int(line)

  return highest_calorie_count


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
