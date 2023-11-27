import os

def part2():
  score = 0
  points = dict(
    X=1,
    Y=2,
    Z=3,
  )
  LOSS = 0
  DRAW = 3
  WIN = 6


  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    (their, result) = line.split(" ")
    their = their.strip()
    result = result.strip()

    if result == "Y": 
      if their == "A":
        score += points["X"] + DRAW
      elif their =="B":
        score += points["Y"] + DRAW
      elif their == "C":
        score += points["Z"] + DRAW
    elif result == "Z":
      if their == "A":
        score += points["Y"] + WIN
      elif their =="B":
        score += points["Z"] + WIN
      elif their == "C":
        score += points["X"] + WIN
    else:
      if their == "A":
        score += points["Z"] + LOSS
      elif their =="B":
        score += points["X"] + LOSS
      elif their == "C":
        score += points["Y"] + LOSS

  return score
  
def part1():
  score = 0
  points = dict(
    X=1,
    Y=2,
    Z=3
  )
  LOSS = 0
  DRAW = 3
  WIN = 6


  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    (their, mine) = line.split(" ")
    their = their.strip()
    mine = mine.strip()

    if (their == "A" and mine == "X") or (their == "B" and mine == "Y") or (their == "C" and mine == "Z"): 
      score += points[mine] + DRAW
    elif (their == "A" and mine == "Y") or (their == "B" and mine == "Z") or (their == "C" and mine == "X"):
      score += points[mine] + WIN
    else:
      score += points[mine] + LOSS

  return score


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
