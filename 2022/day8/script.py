import os


def am_i_visible(forest, tree_height, column, row, direction, depth=0):
  parent_row = None
  parent_column = None
  if direction == 'top':
    if row == 0:
      return (True, depth)
    parent_row = row - 1
    parent_column = column
  elif direction == 'bottom':
    if row == len(forest) - 1:
      return (True, depth)
    parent_row = row + 1
    parent_column = column
  if direction == 'left':
    if column == 0:
      return (True, depth)
    parent_row = row
    parent_column = column - 1
  elif direction == 'right':
    if column == len(forest[0]) - 1:
      return (True, depth)
    parent_row = row
    parent_column = column + 1

  parent = forest[parent_row][parent_column]
  if parent["height"] >= tree_height:
    return (False, depth+1)

  return am_i_visible(forest, tree_height, parent_column, parent_row,
                      direction, depth + 1)


def build_forest():
  forest = []
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")

  for row, line in enumerate(file):
    line = line.strip()
    forest.append([])
    for c in line:
      forest[row].append(dict(height=int(c), visible=None))

  for row, forest_row in enumerate(forest):
    for column, tree in enumerate(forest_row):
      # Check top
      top, top_depth = am_i_visible(forest, forest[row][column]['height'],
                                    column, row, 'top')
      # Check bottom
      bottom, bottom_depth = am_i_visible(forest, forest[row][column]['height'], column, row, 'bottom')
      # Check left
      left, left_depth = am_i_visible(forest, forest[row][column]['height'], column, row, 'left')
      # Check right
      right, right_depth = am_i_visible(forest, forest[row][column]['height'], column, row, 'right')
      forest[row][column]['visible'] = top or bottom or left or right
      forest[row][column][
        "scenic_score"] = top_depth * bottom_depth * left_depth * right_depth
  return forest


def part2():
  forest = build_forest()
  top = 0
  for forest_row in forest:
    for tree in forest_row:
      if tree['scenic_score'] > top:
        top = tree["scenic_score"]

  return top


def part1():
  forest = build_forest()
  visible = 0
  for forest_row in forest:
    for tree in forest_row:
      if tree['visible']:
        visible += 1

  return visible


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))
