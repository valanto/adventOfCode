import os


def find_increments(windows):
    increments = 0
    last_number = None
    for win in windows:
        if last_number and last_number < win:
            increments += 1
        last_number = win
    return increments


def part1():
    windows = []
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    for line in file:
        windows.append(int(line.strip()))

    return find_increments(windows)


def part2():
    windows = []
    window_position = [0, -1, -2, -3]
    window_sums = [0, 0, 0, 0]
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    for line in file:
        depth = int(line.strip())
        for w in range(len(window_position)):
            if window_position[w] >= 0:
                window_sums[w] += depth
            if window_position[w] == 2:
                windows.append(window_sums[w])
                window_position[w] = -1
                window_sums[w] = 0
            else:
                window_position[w] += 1

    return find_increments(windows)


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))