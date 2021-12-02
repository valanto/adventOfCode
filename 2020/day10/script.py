import os
import re
from itertools import combinations


def get_adapters():
    adapters = []
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    for line in file:
        adapter = int(line.strip())
        adapters.append(adapter)

    file.close()
    adapters.sort()
    return adapters


def differences(adapters):
    one = 0
    two = 0
    three = 0

    joltage = 0

    for adapter in adapters:
        diff = adapter - joltage
        joltage = adapter
        if diff == 1:
            one += 1
        elif diff == 2:
            two += 1
        elif diff == 3:
            three += 1
        else:
            print("other: {0}: {1} - {2}".format(diff, adapter, joltage))

    # final adapter
    three += 1

    return (one, two, three)


def all_lists(items):
    comb = []
    for n in range(0, len(items) + 1):
        for i in combinations(items, n):
            comb.append(list(i))

    return comb


def combo_check(adapters, end, joltage=0):
    if joltage + 3 >= end:
        return True

    if len(adapters) == 0:
        return False

    adapter = adapters.pop(0)
    if adapter - joltage <= 3:
        return combo_check(adapters, end, adapter)

    return False


# def combos(adapters, combo, end):
#     combo_list = []

#     adapters_combos = all_lists(adapters)

#     for combo in adapters_combos:
#         for adapter in combo:
#             if adapter <= 3:
#                 if combo_check(combo, end, adapter):
#                     combo_list.append(combo)

#     return combo_list


def sublists(l):
    sublist = []

    for i in range(len(l) + 1):

        for j in range(i + 1, len(l) + 1):

            sli = l[i:j]  # make a slice of the subarray
            sublist.append(sli)  # add it to the list of sublists

    return sublist


existing_combos = []
cache = []


def add_to_cache(adapters):
    for sub_adapters in sublists(adapters):
        key = ",".join([str(sa) for sa in sub_adapters])
        if key not in cache:
            cache.append(key)


def combos(adapters, end):
    combos_list = []
    joltage = 0

    for adapter in adapters:
        adapters_copy = adapters.copy()
        adapters_copy.remove(adapter)

        if adapters_copy not in existing_combos:
            for ac in adapters_copy:
                if ac - joltage > 3:
                    break
                joltage = ac

            if joltage + 3 >= end:
                combos_list.append(adapters_copy)
                existing_combos.append(adapters_copy)
                add_to_cache(adapters_copy)
                combos_list = combos_list + combos(adapters_copy, end)

    return combos_list


adapters = get_adapters()

(one, two, three) = differences(adapters)
print("part1: {0}*{1}={2}".format(one, three, one * three))

combos_list = combos(adapters, max(adapters) + 3)


print("part2: {0}".format(len(combos_list) + 1))
