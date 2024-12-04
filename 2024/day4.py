import os
import re

def find_xmas():
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  letters = []
  positions = dict()
  for lineIdx, line in enumerate(file):
    if line.strip():
      for characterIdx, letter in enumerate(line.strip()):
        if letter in ['X','M','A','S']:
          letters.append((letter, lineIdx, characterIdx))
          if lineIdx not in positions:
            positions[lineIdx] = dict()
          positions[lineIdx][characterIdx] = letter

  return (letters, positions)

def check(positions, letters, l, c, step):
  (v, h) = step
  v_step=l
  h_step=c
  for x in letters:
    if v_step not in positions or h_step not in positions[v_step] or positions[v_step][h_step] != x:
      return False
    v_step=v_step+v
    h_step=h_step+h

  return True

def part2():
  total = 0
  (letters, positions) = find_xmas()
  for (letter, l, c) in letters:
    if (check(positions,['M','A','S'],l,c,(1,1)) or check(positions,['S','A','M'],l,c,(1,1))) and (check(positions,['M','A','S'],l,c+2,(1,-1)) or check(positions,['S','A','M'],l,c+2,(1,-1))):
        total += 1


  return total

def part1():
  total = 0
  (letters, positions) = find_xmas()
  for (letter, l, c) in letters:
    if letter == 'X':
      # horizontal
      if check(positions,['X','M','A','S'],l,c,(0,1)):
        total += 1
      # horizontal_reverse
      if check(positions,['X','M','A','S'],l,c,(0,-1)):
        total += 1
      # vertical
      if check(positions,['X','M','A','S'],l,c,(1,0)):
        total += 1
      # vertical_reverse
      if check(positions,['X','M','A','S'],l,c,(-1,0)): 
        total += 1
      # diagonal_down
      if check(positions,['X','M','A','S'],l,c,(1,1)):
        total += 1
      # diagonal_up
      if check(positions,['X','M','A','S'],l,c,(-1,1)): 
        total += 1
      # diagonal_reverse_up
      if check(positions,['X','M','A','S'],l,c,(1,-1)):
        total += 1
      # diagonal_reverse_down
      if check(positions,['X','M','A','S'],l,c,(-1,-1)): 
        total += 1

  return total

print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
