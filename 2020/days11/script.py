import os
import re
import copy


def get_table():
    table = []
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")

    for line in file:
        line = line.strip()

        row = []
        for p in line:
            if p == ".":
                row.append(0)
            if p == "L":
                row.append(1)
        table.append(row)

    file.close()
    return table


def adj(table, column, row):
    if column < 0 or row < 0 or column >= len(table) or row >= len(table[0]):
        return None

    return table[column][row]


def is_occupied(table, column, row):
    return adj(table, column, row) is not None and adj(table, column, row) == 2


def is_not_occupied(table, column, row):
    return adj(table, column, row) is None or adj(table, column, row) == 1


def has_any_occupied_adj(table, column, row):
    if (
        is_occupied(table, column - 1, row - 1)
        or is_occupied(table, column, row - 1)
        or is_occupied(table, column + 1, row - 1)
        or is_occupied(table, column + 1, row)
        or is_occupied(table, column + 1, row + 1)
        or is_occupied(table, column, row + 1)
        or is_occupied(table, column - 1, row + 1)
        or is_occupied(table, column - 1, row)
    ):
        return True

    return False


def get_empty_seats(layout):
    change = True

    while change:
        change = False
        rn = 0
        layout_copy = copy.deepcopy(layout)
        for row in layout_copy:
            cn = 0
            for column in row:
                if column == 1 and not has_any_occupied_adj(layout, cn, rn):
                    layout[rn][cn] = 2
                    change = True

                cn += 1

        rn += 1

    print(layout)


print(get_empty_seats(get_table()))
# print("part1: ".format(one, three, one * three))
