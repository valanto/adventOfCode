def part1():
  forest = build_forest()
  visible = 0
  for forest_row in forest:
    for tree in forest_row:
      if tree['visible']:
        visible += 1

  return visible


print("part1: {0}".format(part1()))