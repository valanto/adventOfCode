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

def jump(position, compact, obstacle):
  (y,x,d) = position
  if d ==0 and x != obstacle[1]:
    return (y-compact[(y,x)][d], x, d)
  elif d == 1 and y != obstacle[0]:
    return (y, x+compact[(y,x)][d], d) 
  elif d ==2 and x != obstacle[1]:
    return (y+compact[(y,x)][d], x, d)
  elif d == 3 and y != obstacle[0]:
    return (y, x-compact[(y,x)][d], d) 
  
  return move(position)

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

def find_distance(positions, y, x, d):
  count = 0
  while y > 0 and x > 0 and y < len(positions) and x < len(positions[y]) and positions[y][x] == 0:
    (y, x, d) = move((y, x, d))
    count+=1
  return count


def compact_positions(positions):
  compact = dict()
  for y in range(len(positions)):
    for x in range(len(positions[y])):
      compact[(y,x)]=dict()
      compact[(y,x)][0]=find_distance(positions, y, x, 0)
      compact[(y,x)][1]=find_distance(positions,y, x, 1)
      compact[(y,x)][2]=find_distance(positions,y, x, 2)
      compact[(y,x)][3]=find_distance(positions,y, x, 3)
  return compact
    
def part2():
  distinct = get_distinct()
  obstacles=[]
  (positions, current) = generate_list()
  compact = compact_positions(positions)
  start = (current[0], current[1], current[2])
  d_idx = 0
  distincts_in_loop = dict()
  while d_idx < len(distinct):
    (y, x, d) = jump(current, compact, distinct[d_idx])
    if (y, x, d) == current:
      (y, x, d) = move(current)
    if y < 0 or x < 0 or y >= len(positions) or x >= len(positions[y]):  
      d_idx += 1
      distincts_in_loop=dict()
      current =  (start[0], start[1], start[2])
      continue

    if positions[y][x] or (distinct[d_idx][0] == y and distinct[d_idx][1]==x):
      d = d + 1 if d < 3 else 0
      current = (current[0], current[1], d)
    else:
      current=(y, x, d)

    if (current[0], current[1]) in distincts_in_loop:
      if distincts_in_loop[(current[0], current[1])] > 1:
        obstacles.append(distinct[d_idx])
        distincts_in_loop = dict()
        d_idx +=1
        current =  (start[0], start[1], start[2])
      else:
        distincts_in_loop[(current[0], current[1])] += 1
    else:
      distincts_in_loop[(current[0], current[1])]=0
    

  return len(obstacles)


def part1():
  return len(get_distinct())

print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
