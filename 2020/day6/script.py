import os


def group_answers_union():
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    groups = []
    group_yeses = []
    for line in file:
        if line.strip() == "":
            groups.append(len(group_yeses))
            group_yeses = []
        else:
            for c in line.strip():
                if c not in group_yeses:
                    group_yeses.append(c)
    file.close()
    return groups


def group_answers_intersection():
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    groups = []
    group_yeses = []
    first = True
    for line in file:
        if line.strip() == "":
            groups.append(len(group_yeses))
            group_yeses = []
            first = True
        else:
            if first:
                for c in line.strip():
                    if c not in group_yeses:
                        group_yeses.append(c)
            else:
                new_group_yeses = []
                for o in group_yeses:
                    if o in line.strip():
                        new_group_yeses.append(o)
                group_yeses = new_group_yeses
            first = False
    file.close()
    return groups


print("part1: {0}".format(sum(group_answers_union())))
print("part2: {0}".format(sum(group_answers_intersection())))
