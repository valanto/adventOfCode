import os
import re


def parse_bags():
    file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
    bags = dict()
    for line in file:
        matches = re.match(r"^(([a-zA-Z]+\s+)+)bags\s+contain\s+(.*)\.$", line)
        if not matches:
            print("no step1 match: {0}".format(line))

        bag = matches.group(1).strip()
        contentsString = matches.group(3).strip()

        contentBags = dict()

        if contentsString != "no other bags":
            splitString = contentsString.split(", ")
            for entry in splitString:
                entryMatches = re.match(r"(\d+)\s+", entry)
                contentBags[re.sub(r"\d+\s*", "", re.sub(r"\s*bags?$", "", entry.strip()))] = int(
                    entryMatches.group(1).strip()
                )

        bags[bag] = contentBags

    file.close()
    return bags


def bag_compatibility(bags, bag):
    compatible_bags = []
    for b in bags:
        if bag in bags[b]:
            compatible_bags += [b] + bag_compatibility(bags, b)

    return list(dict.fromkeys(compatible_bags))


def bag_requirements(bags, bag):
    required_bags_count = 0
    required_bags = bags[bag]
    for b in required_bags:
        required_bags_count += required_bags[b] + required_bags[b] * bag_requirements(bags, b)

    return required_bags_count


bags = parse_bags()

gold_bag_compatibility = bag_compatibility(bags, "shiny gold")
required_bags = bag_requirements(bags, "shiny gold")

print("part1: {0}".format(len(gold_bag_compatibility)))
print("part2: {0}".format(required_bags))
