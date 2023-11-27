import os

def part2():
  stack = [
    ["D","L","J","R","V","G","F"],
    ["T","P","M","B","V","H","J","S"],
    ["V","H","M","F","D","G","P","C"],
    ["M","D","P","N","G","Q"],
    ["J","L","H","N","F"],
    ["N","F","V","Q","D","G","T","Z"],
    ["F","D","B","L"],
    ["M","J","B","S","V","D","N"],
    ["G","L","D"]
  ]

  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    (_, index, _, from_stack, _, to_stack) = line.strip().split(" ")
    index=int(index)
    from_stack = int(from_stack) - 1
    to_stack = int(to_stack) - 1
    from_index=len(stack[from_stack])-index
    to_index=len(stack[from_stack])

    stack[to_stack] = stack[to_stack] + stack[from_stack][slice(from_index,to_index)]
    stack[from_stack] = stack[from_stack][slice(0, from_index)]


  return "{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(stack[0][len(stack[0])-1], stack[1][len(stack[1])-1], stack[2][len(stack[2])-1], stack[3][len(stack[3])-1],stack[4][len(stack[4])-1],stack[5][len(stack[5])-1],stack[6][len(stack[6])-1],stack[7][len(stack[7])-1],stack[8][len(stack[8])-1])

def part1():
  stack = [
    ["D","L","J","R","V","G","F"],
    ["T","P","M","B","V","H","J","S"],
    ["V","H","M","F","D","G","P","C"],
    ["M","D","P","N","G","Q"],
    ["J","L","H","N","F"],
    ["N","F","V","Q","D","G","T","Z"],
    ["F","D","B","L"],
    ["M","J","B","S","V","D","N"],
    ["G","L","D"]
  ]

  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  for line in file:
    (_, index, _, from_stack, _, to_stack) = line.strip().split(" ")
    index=int(index)
    from_stack = int(from_stack) - 1
    to_stack = int(to_stack) - 1
    for i in range(0, index):
      stack[to_stack].append(stack[from_stack].pop())


  return "{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(stack[0][len(stack[0])-1], stack[1][len(stack[1])-1], stack[2][len(stack[2])-1], stack[3][len(stack[3])-1],stack[4][len(stack[4])-1],stack[5][len(stack[5])-1],stack[6][len(stack[6])-1],stack[7][len(stack[7])-1],stack[8][len(stack[8])-1])


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
