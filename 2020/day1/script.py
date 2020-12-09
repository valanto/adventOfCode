file = open("./input.txt", "r")
numbers = []
for line in file:
  numbers.append(line)
file.close()

for n1 in numbers:
    for n2 in numbers:
        if(int(n1) + int(n2) == 2020):
            print("part1: {0} * {1} = {2}".format(n1, n2, int(n1)*int(n2)))

for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            if(int(n1) + int(n2) + int(n3) == 2020):
                print("part2: {0} * {1} * {2} = {3}".format(n1, n2, n3, int(n1)*int(n2) * int(n3)))
