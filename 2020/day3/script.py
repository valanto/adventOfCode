import re


def tree_counter(right, down):
    file = open("./input.txt", "r")
    number_of_trees = 0
    current_index = right
    next_line = down
    current_line = 0

    for line in file:
        line = line.strip()
        if current_line == next_line:
            index = current_index if current_index < len(line) else current_index % len(line)
            if line[index] == "#":
                number_of_trees += 1

            next_line += down
            current_index += right
        current_line += 1
    file.close()
    return number_of_trees


print("part1: {0}".format(tree_counter(3, 1)))

slope1 = tree_counter(1, 1)
slope2 = tree_counter(3, 1)
slope3 = tree_counter(5, 1)
slope4 = tree_counter(7, 1)
slope5 = tree_counter(1, 2)

print(
    "part2: {0} * {1} * {2} * {3} * {4} = {5}".format(
        slope1, slope2, slope3, slope4, slope5, (slope1 * slope2 * slope3 * slope4 * slope5)
    )
)
