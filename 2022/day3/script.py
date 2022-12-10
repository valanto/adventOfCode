import os
item_priority = dict(
  a=1,
  b=2,
  c=3,
  d=4,
  e=5,
  f=6,
  g=7,
  h=8,
  i=9,
  j=10,
  k=11,
  l=12,
  m=13,
  n=14,
  o=15,
  p=16,
  q=17,
  r=18,
  s=19,
  t=20,
  u=21,
  v=22,
  w=23,
  x=24,
  y=25,
  z=26,
  A=27,
  B=28,
  C=29,
  D=30,
  E=31,
  F=32,
  G=33,
  H=34,
  I=35,
  J=36,
  K=37,
  L=38,
  M=39,
  N=40,
  O=41,
  P=42,
  Q=43,
  R=44,
  S=45,
  T=46,
  U=47,
  V=48,
  W=49,
  X=50,
  Y=51,
  Z=52
)

def part2():
  sum=0
  group = []
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    line = line.strip()
    char_count = dict()
    for c in line:
      if c not in char_count:
        char_count[c] = 1
      else:
        char_count[c] +=1
    group.append(char_count)

    if len(group) == 3:
      for c in group[0].keys():
        if c in group[1].keys() and c in group[2].keys():
          sum += item_priority[c] 
          break
      group = []


  return sum

def part1():
  sum=0

  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    line = line.strip()
    compartment1 = line[slice(0, len(line)//2)]
    compartment2 = line[slice(len(line)//2, len(line))]
    common_character = None
    for character in compartment1:
      if character in compartment2:
        common_character = character
        
    sum += item_priority[common_character]

  return sum


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
