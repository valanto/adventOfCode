import os
import re
import math

def direction(c):
  directions = ['^','>', 'V', '<']
  if c in directions:
    return directions.index(c)
  return None

def generate_list():
  positions = []
  current = (0,0, 0)
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for l,line in enumerate(file):
    row = []
    for r, c in enumerate(line.strip()):
      if c == '#':
        row.append(1)
      elif c=='.':
        row.append(0)
      else:
        current = (l,r, direction(c))
    positions.append(row)

  return (positions, current)

def move(position):
  (y,x,d) = position
  if d == 0:
    return (y-1, x, d)
  elif d == 1:
    return (y, x+1, d)
  elif d == 2:
    return (y+1, x, d)
  elif d == 3:
    return (y, x-1, d)

def get_distinct():
  distinct=[]
  (positions, current) = generate_list()
  inside = True
  while inside:
    (y, x, d) = move(current)
    if y < 0 or x < 0 or y >= len(positions) or x >= len(positions[y]):
      inside=False
      break
    if positions[y][x]:
      d = d + 1 if d < 3 else 0
      current = (current[0], current[1], d)
    else:
      current=(y, x, d)
    if (current[0], current[1]) not in distinct:
      distinct.append((current[0], current[1]))
  
  return distinct

def part2():
  distinct = get_distinct()
  obstacles=[]
  (positions, current) = generate_list()
  start = (current[0], current[1], current[2])
  d_idx = 0
  once = False
  while d_idx < len(distinct):
    (y, x, d) = move(current)
    if y < 0 or x < 0 or y >= len(positions) or x >= len(positions[y]):  
      d_idx += 1
      once = False
      current =  (start[0], start[1], start[2])
      print(math.round(d_idx/len(distinct) * 100))

      continue

    if positions[y][x] or (distinct[d_idx][0] == y and distinct[d_idx][1]==x):
      d = d + 1 if d < 3 else 0
      current = (current[0], current[1], d)
    else:
      current=(y, x, d)

    if distinct[d_idx][0] == y and distinct[d_idx][1] == x:
      if once:
        obstacles.append(distinct[d_idx])
        once = False
        d_idx +=1
        current =  (start[0], start[1], start[2])
        print(math.round(d_idx/len(distinct) * 100))
      else:
        once = True
    

  return len(obstacles)


def part1():
  return len(get_distinct())

print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
