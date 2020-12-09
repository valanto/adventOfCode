import os


def binary_search(text, character, start, end):
    for t in text:
        next_step = int((end - start + 1) / 2)
        if t == character:
            end = end - next_step
        else:
            start = start + next_step

    return start


file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")

max = 0
ids = []

for line in file:
    row = binary_search(line[0:7], "F", 0, 127)
    column = binary_search(line[7:10], "L", 0, 7)

    seat_id = row * 8 + column
    if seat_id > max:
        max = seat_id
    ids.append(seat_id)

print("part1: {0}".format(max))

ids.sort()

previous = None
for id in ids:
    if id > 15 and id < (127 * 8):
        if previous and previous != id - 1:
            print("part2: {0}".format(id - 1))
        previous = id

file.close()
